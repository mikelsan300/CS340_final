import sqlite3

def create_tables(conn):
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS workout_plans (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS exercises (
            id INTEGER PRIMARY KEY,
            workout_plan_id INTEGER,
            name TEXT NOT NULL,
            sets INTEGER,
            reps_min INTEGER,
            reps_max INTEGER,
            duration_seconds INTEGER,
            FOREIGN KEY (workout_plan_id) REFERENCES workout_plans (id)
        )
    """)

    conn.commit()

def insert_data(conn):
    cursor = conn.cursor()

    # Workout plans data
    workout_plans = [
        (1, "Strength Training - Beginner"),
        (2, "Cardio - Beginner"),
        (3, "Strength Training - Advanced"),
    ]

    # Exercises data
    exercises = [
        (1, 1, "Squats", 3, 10, 12, None),
        (2, 1, "Push-ups", 3, 10, 15, None),
        (3, 1, "Lunges", 3, 10, 12, None),
        (4, 1, "Plank", 3, 30, 60, None),
        
        (5, 2, "Jumping Jacks", 3, 30, 60, None),
        (6, 2, "High Knees", 3, 30, 60, None),
        (7, 2, "Mountain Climbers", 3, 30, 60, None),
        (8, 2, "Burpees", 3, 10, 15, None),
        
        (9, 3, "Barbell Squats", 4, 6, 8, None),
        (10, 3, "Deadlifts", 4, 6, 8, None),
        (11, 3, "Bench Press", 4, 6, 8, None),
        (12, 3, "Pull-ups", 4, 6, 8, None),
    ]

    cursor.executemany("""
        INSERT INTO workout_plans (id, name)
        VALUES (?, ?)
    """, workout_plans)

    cursor.executemany("""
        INSERT INTO exercises (id, workout_plan_id, name, sets, reps_min, reps_max, duration_seconds)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, exercises)

    conn.commit()

def main():
    conn = sqlite3.connect("placeholder_workoutplans.db")
    create_tables(conn)
    insert_data(conn)
    conn.close()

if __name__ == "__main__":
    main()
