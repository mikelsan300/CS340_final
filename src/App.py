from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras_tuner.tuners import RandomSearch
from tensorflow import keras
from tensorflow.keras import layers



def fitness_level(df):
    output = []

    for _, row in df.iterrows():
        
        age, daysIntensePhysAct, minsIntensePhysAct, daysModeratePhysAct, minsModeratePhysAct, weight, height, BMI = row


        # Calculate weighted activity level based on intense and moderate activity
        activity_level = 2.5 * (daysIntensePhysAct * minsIntensePhysAct) + (daysModeratePhysAct * minsModeratePhysAct)
        BMI = weight / (height ** 2)
        # Determine weight goal based on BMI
        weight_goal = "lose_weight" if BMI > 25.0 else "gain_muscle"

        # Classify fitness level based on activity level and age
        if activity_level < 150.0 * age / 100.0:
            fitness_level = "low"
        else:
            fitness_level = "advanced"

        # Assign fitness number based on weight goal and fitness level
        if weight_goal == "lose_weight" and fitness_level == "low":
            number = max(1, min(99, 1 + (activity_level % 100.0)))
        elif weight_goal == "lose_weight" and fitness_level == "advanced":
            number = max(100, min(199, 100 + (activity_level % 100.0)))
        elif weight_goal == "gain_muscle" and fitness_level == "low":
            number = max(200, min(299, 200 + (activity_level % 100.0)))
        else: # weight_goal == "gain_muscle" and fitness_level == "advanced"
            number = max(300, min(399, 300 + (activity_level % 100.0)))

        output.append(number)
    
    return output

app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'])


data = pd.read_csv('output.csv')

# Replace 'input_file.xpt' with the path to your .XPT file
gender_age_XPT = 'DEMO_J.XPT'
physical_activity_XPT = 'PAQ_J.XPT'
weight_height_XPT = 'BMX_J.XPT'

# Replace 'output_file.csv' with the desired output CSV file path
gender_age_CSV = 'DEMO_J.csv'
physical_activity_CSV = 'PAQ_J.csv'
weight_height_CSV = 'BMX_J.csv'

# Read the .XPT file using pandas
df_genAge = pd.read_sas(gender_age_XPT, format='xport')
df_physAct = pd.read_sas(physical_activity_XPT, format='xport')
df_wh = pd.read_sas(weight_height_XPT, format='xport')

# Write the DataFrame to a CSV file
df_genAge.to_csv(gender_age_CSV, index=False)
df_physAct.to_csv(physical_activity_CSV, index=False)
df_wh.to_csv(weight_height_CSV, index=False)

df_genAge = df_genAge.drop(columns=['SDDSRVYR', 'RIDSTATR','RIDAGEMN',
       'RIDRETH1', 'RIDRETH3', 'RIDEXMON', 'RIDEXAGM', 'DMQMILIZ', 'DMQADFC',
       'DMDBORN4', 'DMDCITZN', 'DMDYRSUS', 'DMDEDUC3', 'DMDEDUC2', 'DMDMARTL',
       'RIDEXPRG', 'SIALANG', 'SIAPROXY', 'SIAINTRP', 'FIALANG', 'FIAPROXY',
       'FIAINTRP', 'MIALANG', 'MIAPROXY', 'MIAINTRP', 'AIALANGA', 'DMDHHSIZ',
       'DMDFMSIZ', 'DMDHHSZA', 'DMDHHSZB', 'DMDHHSZE', 'DMDHRGND', 'DMDHRAGZ',
       'DMDHREDZ', 'DMDHRMAZ', 'DMDHSEDZ', 'WTINT2YR', 'WTMEC2YR', 'SDMVPSU',
       'SDMVSTRA', 'INDHHIN2', 'INDFMIN2', 'INDFMPIR' ])

df_physAct = df_physAct.drop(columns=['PAQ605', 'PAQ610', 'PAD615', 'PAQ620', 'PAQ625', 'PAD630',
       'PAQ635', 'PAQ640', 'PAD645', 'PAQ650','PAQ665', 'PAD680'])

df_wh = df_wh.drop(columns=['BMDSTATS', 'BMIWT', 'BMXRECUM', 'BMIRECUM', 'BMXHEAD',
       'BMIHEAD', 'BMIHT', 'BMXLEG', 'BMILEG', 'BMXARML',
       'BMIARML', 'BMXARMC', 'BMIARMC', 'BMXWAIST', 'BMIWAIST', 'BMXHIP',
       'BMIHIP'])

df_genAge = df_genAge.rename(columns={'SEQN':'Id', 'RIAGENDR' : 'sex', 'RIDAGEYR' : 'age'})
df_physAct = df_physAct.rename(columns={'SEQN':'Id', 'PAQ655': 'daysIntensePhysAct', 'PAD660':'minsIntensePhysAct', 'PAQ670':'daysModeratePhysAct', 'PAD675':'minsModeratePhysAct'})
df_wh = df_wh.rename(columns={'SEQN':'Id', 'BMXWT' : 'weight', 'BMXHT' : 'height', 'BMXBMI':'BMI'})


merged_df = pd.merge(df_genAge, df_physAct[['Id', 'daysIntensePhysAct', 'minsIntensePhysAct', 'daysModeratePhysAct', 'minsModeratePhysAct']], on='Id')
merged_df = pd.merge(merged_df, df_wh, on='Id')
df = merged_df.fillna(0)
data = data[data["height"] != 0]
data.drop([ 'Id', 'sex'], axis=1, inplace=True)

data['fitness_score'] = fitness_level(data)

X = data[['age', 'daysIntensePhysAct', 'minsIntensePhysAct',	'daysModeratePhysAct',	'minsModeratePhysAct',	'weight',	'height',	'BMI']]
y = data['fitness_score']

    # Split data into training and testing sets




    # Preprocess the data



def suggest_workout(fitness_level):
    if 1.0 <= fitness_level <= 99.0:
        return "Weight Loss: Beginner"
    elif 100.0 <= fitness_level <= 199.0:
        return "Weight Loss: Advanced"
    elif 200.0 <= fitness_level <= 299.0:
        return "Muscle Gain: Beginner"
    elif 300.0 <= fitness_level <= 399.0:
        return "Muscle Gain: Advanced"
    else:
        return "Invalid fitness level."


def build_model(hp):
    model = keras.Sequential()
    model.add(layers.Dense(units=hp.Int('units_input', min_value=32, max_value=128, step=32),
                           input_dim=X_train.shape[1],
                           activation='relu'))
    
    for i in range(hp.Int('num_layers', min_value=1, max_value=3)):
        model.add(layers.Dense(units=hp.Int(f'units_{i}', min_value=32, max_value=128, step=32),
                               activation='relu'))
    
    model.add(layers.Dense(1, activation='linear'))

    optimizer = keras.optimizers.Adam(learning_rate=hp.Float('learning_rate', min_value=1e-4, max_value=1e-2, sampling='LOG'))
    model.compile(loss='mean_squared_error', optimizer=optimizer)
    
    return model




def get_workout(workout_plan_id):
    # Connect to the SQLite database
    conn = sqlite3.connect("workouts.db")

    cursor = conn.cursor()

    # Execute the SQL query
    cursor.execute("""
        SELECT workout_id, workout_description, fitness_goal
        FROM workout_plans
        WHERE workout_id = ?
    """, (workout_plan_id,))

    # Fetch the results
    results = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Return the workout plan details and exercises
    return results



def recommend_workout_plan(score):
    min_score = 1
    max_score = 399
    num_workouts = 40

    # Calculate the size of each block
    block_size = (max_score - min_score + 1) / num_workouts

    # Find the block the score falls into
    block_index = int((int(score) - min_score) // block_size)

    # Assign the workout ID (1-based index)
    workout_id = block_index + 1

    return workout_id
    



def recommend(user_input):

    age = int(user_input['age'])
    weight = float(user_input['weight'])
    height = float(user_input['height'])
    BMI = weight / (height ** 2)
    daysIntensePhysAct = int(user_input['intenseDays'])
    minsIntensePhysAct = int(user_input['intenseMinutes'])
    daysModeratePhysAct = int(user_input['moderateDays'])
    minsModeratePhysAct = int(user_input['moderateMinutes'])

    new_data = {
    
    'age': [age],
    'daysIntensePhysAct': [daysIntensePhysAct],
    'minsIntensePhysAct': [daysIntensePhysAct],
    'daysModeratePhysAct': [daysModeratePhysAct],
    'minsModeratePhysAct': [daysModeratePhysAct], 
    'weight': [weight],
    'height': [height],
    'BMI': [BMI]
    }

    new_features_df = pd.DataFrame(new_data)

    #scale new features
    print(new_features_df)
    scaled_new_features = feature_scaler.transform(new_features_df)
    # Convert the scaled features back to a DataFrame
    scaled_new_features_df = pd.DataFrame(scaled_new_features, columns=new_features_df.columns)

    #make prediction
    scaled_user_pred = model.predict(scaled_new_features_df)

    #turn scaled prediction into original fitness_level score
    original_user_pred = target_scaler.inverse_transform(scaled_user_pred)

    #output workout
    workout = suggest_workout(original_user_pred)
    print(workout)
    print(original_user_pred)
    
    workout_plan_id = recommend_workout_plan(original_user_pred)
    workout_data = get_workout(workout_plan_id)

    if not workout_data:
        return None

    workout = {
        "workout_id": workout_data[0][0],
        "workout_description": workout_data[0][1],
        "fitness_goal": workout_data[0][2],
    }
    
    return workout

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

feature_scaler = StandardScaler()
X_train_scaled = feature_scaler.fit_transform(X_train)
X_test_scaled = feature_scaler.transform(X_test)

# Convert the target Series objects to NumPy arrays
y_train_np = np.array(y_train)
y_test_np = np.array(y_test)

target_scaler = StandardScaler()
y_train_scaled = target_scaler.fit_transform(y_train_np.reshape(-1, 1)).flatten()
y_test_scaled = target_scaler.transform(y_test_np.reshape(-1, 1)).flatten()

# Define the neural network model
model = Sequential()
model.add(Dense(32, input_dim=X_train_scaled.shape[1], activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='linear'))

# Compile the model
optimizer = Adam(learning_rate=0.001)
model.compile(loss='mean_squared_error', optimizer=optimizer)

# Train the model
model.fit(X_train_scaled, y_train_scaled, epochs=100, batch_size=32, verbose=1, validation_split=0.1)

# Evaluate the model
mse_test = model.evaluate(X_test_scaled, y_test_scaled)

tuner = RandomSearch(
build_model,
objective='val_loss',
max_trials=10,
executions_per_trial=3,
directory='output',
project_name='Fitness_Level_Prediction'
)

tuner.search_space_summary()
tuner.search(X_train_scaled, y_train_scaled, epochs=50, validation_split=0.1, verbose=1)

tuner.results_summary()
best_hyperparameters = tuner.get_best_hyperparameters(num_trials=1)[0]

best_model = tuner.hypermodel.build(best_hyperparameters)
best_model.fit(X_train_scaled, y_train_scaled, epochs=100, batch_size=32, verbose=1, validation_split=0.1)

@app.route('/recommend', methods=['POST'])
def recommend_api():
    

    input_data = request.get_json()
    

    # Scaling the data
    
    workout_plan = recommend(input_data)

    return jsonify(workout_plan)


if __name__ == "__main__":
    app.run(debug=True)
