from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
CORS(app)

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
       'SDMVSTRA', 'INDHHIN2', 'INDFMIN2', 'INDFMPIR'])

df_physAct = df_physAct.drop(columns=['PAQ605', 'PAQ610', 'PAD615', 'PAQ620', 'PAQ625', 'PAD630',
       'PAQ635', 'PAQ640', 'PAD645', 'PAQ650','PAQ665', 'PAD680'])

df_wh = df_wh.drop(columns=['BMDSTATS', 'BMIWT', 'BMXRECUM', 'BMIRECUM', 'BMXHEAD',
       'BMIHEAD', 'BMIHT', 'BMXLEG', 'BMILEG', 'BMXARML',
       'BMIARML', 'BMXARMC', 'BMIARMC', 'BMXWAIST', 'BMIWAIST', 'BMXHIP',
       'BMIHIP'])

df_genAge = df_genAge.rename(columns={'SEQN':'Id', 'RIAGENDR' : 'sex', 'RIDAGEYR' : 'age'})
df_physAct = df_physAct.rename(columns={'SEQN':'Id', 'PAQ655': 'daysIntensePhysAct', 'PAD660':'minsIntensePhysAct', 'PAQ670':'daysModeratePhysAct', 'PAD675':'minsModeratePhysAct'})
df_wh = df_wh.rename(columns={'SEQN':'Id', 'BMXWT' : 'weight', 'BMXHT' : 'height', 'BMXBMI':'BMI'})

merged_df = pd.merge(df_genAge, df_physAct, on='Id')
merged_df = pd.merge(merged_df, df_wh, on='Id')
df = merged_df.fillna(0)

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

def fitness_level(user_data):
    output = []
    age = int(user_data['age'])
    weight = float(user_data['weight'])
    height = float(user_data['height'])
    bmi = weight / (height **2)
    daysIntensePhysAct = int(user_data['intenseDays'])
    minsIntensePhysAct = int(user_data['intenseMinutes'])
    daysModeratePhysAct = int(user_data['moderateDays'])
    minsModeratePhysAct = int(user_data['moderateMinutes'])


    


    # Calculate weighted activity level based on intense and moderate activity
    activity_level = 1.5 * (daysIntensePhysAct * minsIntensePhysAct) + (daysModeratePhysAct * minsModeratePhysAct)

    # Determine weight goal based on BMI
    weight_goal = "lose_weight" if bmi > 25.0 else "gain_muscle"

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

    return number



def recommend_workout_plan(score):
    min_score = 101
    max_score = 399
    num_workouts = 40

    # Calculate the size of each block
    block_size = (max_score - min_score + 1) / num_workouts

    # Find the block the score falls into
    block_index = int((int(score) - min_score) // block_size)

    # Assign the workout ID (1-based index)
    workout_id = block_index + 1

    return workout_id
    



def recommend(input_data):
    score = fitness_level(input_data)
    workout_plan_id = recommend_workout_plan(score)
    workout_data = get_workout(workout_plan_id)

    if not workout_data:
        return None

    workout = {
        "workout_id": workout_data[0][0],
        "workout_description": workout_data[0][1],
        "fitness_goal": workout_data[0][2],
    }
    
    return workout

@app.route('/recommend', methods=['POST'])
def recommend_api():
    input_data = request.get_json()
    workout_plan = recommend(input_data)
    return jsonify(workout_plan)


if __name__ == "__main__":
    app.run(debug=True)
