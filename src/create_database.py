import sqlite3
#beginner workouts

#muscle gain
BegMuscleGainWorkout1 = """Day 1: Chest and Triceps
Bench Press: 4 sets of 8-10 reps
Incline Dumbbell Press: 3 sets of 8-10 reps
Dips: 3 sets of 8-10 reps
Triceps Pushdown: 3 sets of 8-10 reps
Day 2: Back and Biceps
Pull-ups: 4 sets of 8-10 reps
Bent Over Rows: 3 sets of 8-10 reps
Lat Pulldowns: 3 sets of 8-10 reps
Hammer Curls: 3 sets of 8-10 reps
Day 3: Rest
Day 4: Legs and Shoulders
Squats: 4 sets of 8-10 reps
Leg Press: 3 sets of 8-10 reps
Shoulder Press: 3 sets of 8-10 reps
Lateral Raises: 3 sets of 8-10 reps
Day 5: Rest"""

BegMuscleGainWorkout2 = """Day 1: Full Body
Deadlift: 4 sets of 5 reps
Bench Press: 4 sets of 5 reps
Pull-ups: 4 sets of 5 reps
Squats: 4 sets of 5 reps
Military Press: 4 sets of 5 reps
Day 2: Rest
Day 3: Full Body
Deadlift: 4 sets of 5 reps
Bench Press: 4 sets of 5 reps
Pull-ups: 4 sets of 5 reps
Squats: 4 sets of 5 reps
Military Press: 4 sets of 5 reps
Day 4: Rest
Day 5: Full Body
Deadlift: 4 sets of 5 reps
Bench Press: 4 sets of 5 reps
Pull-ups: 4 sets of 5 reps
Squats: 4 sets of 5 reps
Military Press: 4 sets of 5 reps"""

BegMuscleGainWorkout3 = """Muscle Gain Workout 3:
Day 1: Upper Body
Bench Press: 4 sets of 8-10 reps
Bent Over Rows: 4 sets of 8-10 reps
Military Press: 4 sets of 8-10 reps
Pull-ups: 4 sets of 8-10 reps
Day 2: Lower Body
Squats: 4 sets of 8-10 reps
Deadlift: 4 sets of 8-10 reps
Leg Press: 4 sets of 8-10 reps
Calf Raises: 4 sets of 8-10 reps
Day 3: Rest
Day 4: Upper Body
Incline Dumbbell Press: 4 sets of 8-10 reps
Pendlay Rows: 4 sets of 8-10 reps
Dips: 4 sets of 8-10 reps
Chin-ups: 4 sets of 8-10"""

BegMuscleGainWorkout4 = """Day 1: Chest and Triceps
Push-ups: 3 sets of 12-15 reps
Close Grip Bench Press: 3 sets of 10-12 reps
Chest Fly: 3 sets of 10-12 reps
Skull Crushers: 3 sets of 10-12 reps
Day 2: Back and Biceps
Pull-ups: 3 sets of 10-12 reps
Seated Cable Row: 3 sets of 10-12 reps
Face Pull: 3 sets of 10-12 reps
Concentration Curls: 3 sets of 10-12 reps
Day 3: Rest
Day 4: Legs and Shoulders
Goblet Squat: 3 sets of 12-15 reps
Romanian Deadlift: 3 sets of 10-12 reps
Standing Dumbbell Press: 3 sets of 10-12 reps
Reverse Fly: 3 sets of 10-12 reps"""

BegMuscleGainWorkout5 = """Day 1: Chest, Shoulders, and Triceps
Incline Bench Press: 4 sets of 8-10 reps
Standing Dumbbell Press: 3 sets of 8-10 reps
Weighted Dips: 3 sets of 8-10 reps
Day 2: Rest
Day 3: Legs
Barbell Squats: 4 sets of 8-10 reps
Romanian Deadlift: 4 sets of 8-10 reps
Calf Raises: 4 sets of 8-10 reps
Day 4: Rest
Day 5: Back and Biceps
Barbell Rows: 4 sets of 8-10 reps
Lat Pulldowns: 3 sets of 8-10 reps
Barbell Curls: 3 sets of 8-10 reps"""

BegMuscleGainWorkout6 = """Muscle Gain Workout 6:
Day 1: Full Body
Squats: 3 sets of 6-8 reps
Bench Press: 3 sets of 6-8 reps
Barbell Rows: 3 sets of 6-8 reps
Military Press: 3 sets of 6-8 reps
Day 2: Rest
Day 3: Full Body
Deadlift: 3 sets of 6-8 reps
Incline Dumbbell Press: 3 sets of 6-8 reps
Pull-ups: 3 sets of 6-8 reps
Dips: 3 sets of 6-8 reps
Day 4: Rest
Day 5: Full Body
Front Squats: 3 sets of 6-8 reps
Push Press: 3 sets of 6-8 reps
Pendlay Rows: 3 sets of 6-8 reps
Close Grip Bench Press: 3 sets of 6-8 reps"""

BegMuscleGainWorkout7 = """Day 1: Chest and Biceps
Flat Bench Press: 4 sets of 8-10 reps
Incline Dumbbell Press: 3 sets of 8-10 reps
Chest Fly: 3 sets of 10-12 reps
Barbell Curls: 3 sets of 8-10 reps
Incline Dumbbell Curls: 3 sets of 8-10 reps
Day 2: Legs and Abs
Squats: 4 sets of 8-10 reps
Leg Press: 3 sets of 8-10 reps
Leg Curls: 3 sets of 10-12 reps
Calf Raises: 4 sets of 12-15 reps
Hanging Leg Raises: 3 sets of 10-15 reps
Plank: 3 sets, hold for 45-60 seconds
Day 3: Rest
Day 4: Back and Triceps
Deadlift: 4 sets of 6-8 reps
Bent Over Rows: 3 sets of 8-10 reps
Lat Pulldowns: 3 sets of 8-10 reps
Close Grip Bench Press: 3 sets of 8-10 reps
Triceps Pushdown: 3 sets of 10-12 reps
Day 5: Rest
Day 6: Shoulders and Abs
Military Press: 4 sets of 8-10 reps
Lateral Raises: 3 sets of 10-12 reps
Rear Delt Fly: 3 sets of 10-12 reps
Cable Crunches: 3 sets of 10-15 reps
Russian Twists: 3 sets of 15-20 reps
Day 7: Rest"""

BegMuscleGainWorkout8 = """Day 1: Upper Body A
Bench Press: 4 sets of 6-8 reps
Pull-ups: 4 sets of 6-8 reps
Seated Dumbbell Shoulder Press: 3 sets of 8-10 reps
Barbell Rows: 3 sets of 8-10 reps
Skull Crushers: 3 sets of 10-12 reps
Hammer Curls: 3 sets of 10-12 reps
Day 2: Lower Body A
Squats: 4 sets of 6-8 reps
Romanian Deadlift: 3 sets of 8-10 reps
Leg Press: 3 sets of 10-12 reps
Seated Calf Raises: 4 sets of 12-15 reps
Day 3: Rest
Day 4: Upper Body B
Incline Bench Press: 4 sets of 6-8 reps
Chin-ups: 4 sets of 6-8 reps
Standing Military Press: 3 sets of 8-10 reps
Cable Rows: 3 sets of 8-10 reps
Triceps Pushdown: 3 sets of 10-12 reps
Dumbbell Curls: 3 sets of 10-12 reps
Day 5: Lower Body B
Deadlift: 4 sets of 6-8 reps
Front Squats: 3 sets of 8-10 reps
Leg Curls: 3 sets of 10-12 reps
Standing Calf Raises: 4 sets of 12-15 reps
Day 6: Rest
Day 7: Rest"""

BegMuscleGainWorkout9 = """Day 1: Chest and Back
Bench Press: 4 sets of 8-10 reps
Incline Dumbbell Press: 3 sets of 8-10 reps
Pull-ups: 4 sets of 8-10 reps
Bent Over Rows: 3 sets of 8-10 reps
Day 2: Legs and Abs
Squats: 4 sets of 8-10 reps
Leg Press: 3 sets of 8-10 reps
Leg Curls: 3 sets of 10-12 reps
Calf Raises: 4 sets of 12-15 reps
Hanging Leg Raises: 3 sets of 10-15 reps
Plank: 3 sets, hold for 45-60 seconds
Day 3: Rest
Day 4: Shoulders and Arms
Military Press: 4 sets of 8-10 reps
Lateral Raises: 3 sets of 10-12 reps
Triceps Pushdown: 3 sets of 10-12 reps
Barbell Curls: 3 sets of 10-12 reps
Day 5: Rest"""

BegMuscleGainWorkout10 = """Day 1: Chest and Triceps
Flat Bench Press: 4 sets of 6-8 reps
Incline Dumbbell Press: 3 sets of 6-8 reps
Decline Bench Press: 3 sets of 8-10 reps
Triceps Dips: 3 sets of 8-10 reps
Triceps Pushdown: 3 sets of 10-12 reps
Day 2: Back and Biceps
Deadlift: 4 sets of 6-8 reps
Pull-ups: 4 sets of 6-8 reps
Seated Cable Rows: 3 sets of 8-10 reps
Barbell Curls: 3 sets of 8-10 reps
Hammer Curls: 3 sets of 10-12 reps
Day 3: Rest
Day 4: Legs
Squats: 4 sets of 6-8 reps
Leg Press: 3 sets of 8-10 reps
Leg Curls: 3 sets of 10-12 reps
Calf Raises: 4 sets of 12-15 reps
Day 5: Shoulders and Abs
Standing Military Press: 4 sets of 6-8 reps
Lateral Raises: 3 sets of 10-12 reps
Rear Delt Fly: 3 sets of 10-12 reps
Hanging Leg Raises: 3 sets of 10-15 reps
Russian Twists: 3 sets of 15-20 reps
Day 6: Rest
Day 7: Rest"""

#weight loss
BegWeightLossWorkout1 = """Day 1: Full Body
Bodyweight Squats: 3 sets of 10-12 reps
Push-ups: 3 sets of 10-12 reps (knees or incline if necessary)
Bent Over Rows with Dumbbells: 3 sets of 10-12 reps
Reverse Lunges: 3 sets of 10-12 reps per leg
Plank: 3 sets of 30-45 seconds
Day 2: 20min Steady State Cardio of choice
Day 3: Full Body
Step-ups: 3 sets of 10-12 reps per leg
Incline Dumbbell Press: 3 sets of 10-12 reps
Dumbbell Deadlift: 3 sets of 10-12 reps
Seated Dumbbell Shoulder Press: 3 sets of 10-12 reps
Glute Bridge: 3 sets of 12-15 reps
Day 4: 20min Steady State Cardio of choice
Day 5: Full Body
Goblet Squats: 3 sets of 10-12 reps
Lat Pulldown: 3 sets of 10-12 reps
Dumbbell Bicep Curls: 3 sets of 10-12 reps
Tricep Dips: 3 sets of 10-12 reps (use parallel bars or a sturdy chair)
Bicycle Crunches: 3 sets of 15 reps per side"""

BegWeightLossWorkout2 = """Day 1: Upper Body
Push-ups: 3 sets of 10-12 reps (knees or incline if necessary)
Bent Over Rows with Dumbbells: 3 sets of 10-12 reps
Incline Dumbbell Press: 3 sets of 10-12 reps
Seated Dumbbell Shoulder Press: 3 sets of 10-12 reps
Dumbbell Bicep Curls: 3 sets of 10-12 reps
Tricep Dips: 3 sets of 10-12 reps (use parallel bars or a sturdy chair)
Day 2: 20min Steady State Cardio of choice
Day 3: Lower Body
Bodyweight Squats: 3 sets of 10-12 reps
Reverse Lunges: 3 sets of 10-12 reps per leg
Step-ups: 3 sets of 10-12 reps per leg
Dumbbell Deadlift: 3 sets of 10-12 reps
Glute Bridge: 3 sets of 12-15 reps
Day 4: 20min Steady State Cardio of choice
Day 5: Upper Body (Repeat Day 1)"""

BegWeightLossWorkout3 = """Day 1: Full Body
Warm-up: 5-minute light cardio (jog, brisk walk, or jumping jacks)
Goblet Squats: 3 sets of 10-12 reps
Push-ups: 3 sets of 10-12 reps (knees or incline if necessary)
Bent Over Rows with Dumbbells: 3 sets of 10-12 reps
Reverse Lunges: 3 sets of 10-12 reps per leg
Plank: 3 sets of 30-45 seconds
Day 2: 20min Steady State Cardio of choice
Day 3: Full Body
Warm-up: 5-minute light cardio (jog, brisk walk, or jumping jacks)
Step-ups: 3 sets of 10-12 reps per leg
Incline Dumbbell Press: 3 sets of 10-12 reps
Dumbbell Deadlift: 3 sets of 10-12 reps
Seated Dumbbell Shoulder Press: 3 sets of 10-12 reps
Glute Bridge: 3 sets of 12-15 reps
Day 4: 20min Steady State Cardio of choice
Day 5: Full Body
Warm-up: 5-minute light cardio (jog, brisk walk, or jumping jacks)
Bodyweight Squats: 3 sets of 10-12 reps
Lat Pulldown: 3 sets of 10-12 reps
Dumbbell Bicep Curls: 3 sets of 10-12 reps
Tricep Dips: 3 sets of 10-12 reps (use parallel bars or a sturdy chair)
Bicycle Crunches: 3 sets of 15 reps per side"""

BegWeightLossWorkout4 = """Day 1: Full Body + Core
Warm-up: 5-minute light cardio (jog, brisk walk, or jumping jacks)
Goblet Squats: 3 sets of 10-12 reps
Push-ups: 3 sets of 10-12 reps (knees or incline if necessary)
Bent Over Rows with Dumbbells: 3 sets of 10-12 reps
Reverse Lunges: 3 sets of 10-12 reps per leg
Plank: 3 sets of 30-45 seconds
Russian Twists: 3 sets of 12-15 reps per side
Day 2: Rest
Day 3: Full Body + Cardio
Warm-up: 5-minute light cardio (jog, brisk walk, or jumping jacks)
Step-ups: 3 sets of 10-12 reps per leg
Incline Dumbbell Press: 3 sets of 10-12 reps
Dumbbell Deadlift: 3 sets of 10-12 reps
Seated Dumbbell Shoulder Press: 3 sets of 10-12 reps
Glute Bridge: 3 sets of 12-15 reps
Cardio: 15-20min Steady State Cardio of choice
Day 4: Rest
Day 5: Full Body + Core
Warm-up: 5-minute light cardio (jog, brisk walk, or jumping jacks)
Bodyweight Squats: 3 sets of 10-12 reps
Lat Pulldown: 3 sets of 10-12 reps
Dumbbell Bicep Curls: 3 sets of 10-12 reps
Tricep Dips: 3 sets of 10-12 reps (use parallel bars or a sturdy chair)
Bicycle Crunches: 3 sets of 15 reps per side
Leg Raises: 3 sets of 12-15 reps
Day 6: Rest
Day 7: Full Body + Cardio
Warm-up: 5-minute light cardio (jog, brisk walk, or jumping jacks)
Circuit (3 rounds):
Goblet Squats: 12 reps
Push-ups: 12 reps (knees or incline if necessary)
Bent Over Rows with Dumbbells: 12 reps
Reverse Lunges: 12 reps per leg
Plank: 30-45 seconds
Cardio: 15-20min Steady State Cardio of choice"""

BegWeightLossWorkout4 = """Day 1: Upper Body
Warm-up: 5-minute light cardio (jog, brisk walk, or jumping jacks)
Push-ups: 3 sets of 10-12 reps (knees or incline if necessary)
Bent Over Rows with Dumbbells: 3 sets of 10-12 reps
Incline Dumbbell Press: 3 sets of 10-12 reps
Seated Dumbbell Shoulder Press: 3 sets of 10-12 reps
Dumbbell Bicep Curls: 3 sets of 10-12 reps
Tricep Dips: 3 sets of 10-12 reps (use parallel bars or a sturdy chair)
Day 2: Lower Body + Cardio
Warm-up: 5-minute light cardio (jog, brisk walk, or jumping jacks)
Bodyweight Squats: 3 sets of 10-12 reps
Reverse Lunges: 3 sets of 10-12 reps per leg
Step-ups: 3 sets of 10-12 reps per leg
Dumbbell Deadlift: 3 sets of 10-12 reps
Glute Bridge: 3 sets of 12-15 reps
Cardio: 15-20min Steady State Cardio of choice
Day 3: Rest
Day 4: Upper Body
Warm-up: 5-minute light cardio (jog, brisk walk, or jumping jacks)
Lat Pulldown: 3 sets of 10-12 reps
Push-ups: 3 sets of 10-12 reps (knees or incline if necessary)
Bent Over Rows with Dumbbells: 3 sets of 10-12 reps
Incline Dumbbell Press: 3 sets of 10-12 reps
Seated Dumbbell Shoulder Press: 3 sets of 10-12 reps
Dumbbell Bicep Curls: 3 sets of 10-12 reps
Tricep Dips: 3 sets of 10-12 reps (use parallel bars or a sturdy chair)
Day 5: Lower Body + Cardio
Warm-up: 5-minute light cardio (jog, brisk walk, or jumping jacks)
Goblet Squats: 3 sets of 10-12 reps
Reverse Lunges: 3 sets of 10-12 reps per leg
Step-ups: 3 sets of 10-12 reps per leg
Dumbbell Deadlift: 3 sets of 10-12 reps
Glute Bridge: 3 sets of 12-15 reps
Cardio: 15-20min Steady State Cardio of choice"""

BegWeightLossWorkout5 = """Day 1: Full Body Circuit
Warm-up: 5-minute light cardio (jog, brisk walk, or jumping jacks)
Circuit (3 rounds, 45 seconds per exercise with 15 seconds rest between exercises):
Goblet Squats
Push-ups (knees or incline if necessary)
Bent Over Rows with Dumbbells
Reverse Lunges (alternate legs)
Plank
Jumping Jacks
Day 2: Rest
Day 3: Full Body Circuit
Warm-up: 5-minute light cardio (jog, brisk walk, or jumping jacks)
Circuit (3 rounds, 45 seconds per exercise with 15 seconds rest between exercises):
Step-ups (alternate legs)
Incline Dumbbell Press
Dumbbell Deadlift
Seated Dumbbell Shoulder Press
Glute Bridge
High Knees
Day 4: Rest
Day 5: Full Body Circuit
Warm-up: 5-minute light cardio (jog, brisk walk, or jumping jacks)
Circuit (3 rounds, 45 seconds per exercise with 15 seconds rest between exercises):
Bodyweight Squats
Lat Pulldown
Dumbbell Bicep Curls
Tricep Dips (use parallel bars or a sturdy chair)
Bicycle Crunches
Mountain Climbers"""

BegWeightLossWorkout6 = """Day 1: Full Body + Cardio
Warm-up: 5-minute light cardio (jog, brisk walk, or jumping jacks)
Bodyweight Squats: 3 sets of 10-12 reps
Push-ups: 3 sets of 10-12 reps (knees or incline if necessary)
Bent Over Rows with Dumbbells: 3 sets of 10-12 reps
Reverse Lunges: 3 sets of 10-12 reps per leg
Cardio: 20min Steady State Cardio of choice
Day 2: Rest
Day 3: Full Body + Core
Warm-up: 5-minute light cardio (jog, brisk walk, or jumping jacks)
Goblet Squats: 3 sets of 10-12 reps
Incline Dumbbell Press: 3 sets of 10-12 reps
Dumbbell Deadlift: 3 sets of 10-12 reps
Seated Dumbbell Shoulder Press: 3 sets of 10-12 reps
Plank: 3 sets of 30-45 seconds
Russian Twists: 3 sets of 12-15 reps per side
Day 4: Rest
Day 5: Full Body + Cardio
Warm-up: 5-minute light cardio (jog, brisk walk, or jumping jacks)
Step-ups: 3 sets of 10-12 reps per leg
Lat Pulldown: 3 sets of 10-12 reps
Dumbbell Bicep Curls: 3 sets of 10-12 reps
Tricep Dips: 3 sets of 10-12 reps (use parallel bars or a sturdy chair)
Cardio: 20min Steady State Cardio of choice
Day 6: Rest
Day 7: Full Body + Core
Warm-up: 5-minute light cardio (jog, brisk walk, or jumping jacks)
Bodyweight Squats: 3 sets of 10-12 reps
Push-ups: 3 sets of 10-12 reps (knees or incline if necessary)
Bent Over Rows with Dumbbells: 3 sets of 10-12 reps
Reverse Lunges: 3 sets of 10-12 reps per leg
Bicycle Crunches: 3 sets of 15 reps per side
Leg Raises: 3 sets of 12-15 reps"""

BegWeightLossWorkout7 = """Day 1: Full Body Circuit
Warm-up: 5-minute light cardio (jog, brisk walk, or jumping jacks)
Circuit (3 rounds, 45 seconds per exercise with 15 seconds rest between exercises):
Goblet Squats
Push-ups (knees or incline if necessary)
Bent Over Rows with Dumbbells
Reverse Lunges (alternate legs)
Plank
Jumping Jacks
Day 2: 20min Steady State Cardio of choice
Day 3: Full Body Circuit
Warm-up: 5-minute light cardio (jog, brisk walk, or jumping jacks)
Circuit (3 rounds, 45 seconds per exercise with 15 seconds rest between exercises):
Step-ups (alternate legs)
Incline Dumbbell Press
Dumbbell Deadlift
Seated Dumbbell Shoulder Press
Glute Bridge
High Knees
Day 4: 20min Steady State Cardio of choice
Day 5: Full Body Circuit
Warm-up: 5-minute light cardio (jog, brisk walk, or jumping jacks)
Circuit (3 rounds, 45 seconds per exercise with 15 seconds rest between exercises):
Bodyweight Squats
Lat Pulldown
Dumbbell Bicep Curls
Tricep Dips (use parallel bars or a sturdy chair)
Bicycle Crunches
Mountain Climbers"""

BegWeightLossWorkout8 = """Day 1: Upper Body
Warm-up: 5-minute light cardio (jog, brisk walk, or jumping jacks)
Push-ups: 3 sets of 10-12 reps (knees or incline if necessary)
Dumbbell Bench Press: 3 sets of 10-12 reps
Dumbbell Rows: 3 sets of 10-12 reps
Seated Dumbbell Shoulder Press: 3 sets of 10-12 reps
Dumbbell Bicep Curls: 3 sets of 10-12 reps
Tricep Dips (use parallel bars or a sturdy chair): 3 sets of 10-12 reps
Day 2: Lower Body
Warm-up: 5-minute light cardio (jog, brisk walk, or jumping jacks)
Goblet Squats: 3 sets of 10-12 reps
Dumbbell Deadlift: 3 sets of 10-12 reps
Walking Lunges: 3 sets of 10-12 reps per leg
Glute Bridge: 3 sets of 10-12 reps
Calf Raises: 3 sets of 15-20 reps
Day 3: Rest
Day 4: 20min Steady State Cardio of choice
Day 5: Full Body
Warm-up: 5-minute light cardio (jog, brisk walk, or jumping jacks)
Circuit (3 rounds, 45 seconds per exercise with 15 seconds rest between exercises):
Bodyweight Squats
Push-ups (knees or incline if necessary)
Bent Over Rows with Dumbbells
Reverse Lunges (alternate legs)
Plank
Jumping Jacks"""

BegWeightLossWorkout9 = """Day 1: Bodyweight Circuit
Warm-up: 5-minute light cardio (jog, brisk walk, or jumping jacks)
Circuit (3 rounds, 45 seconds per exercise with 15 seconds rest between exercises):
Bodyweight Squats
Push-ups (knees or incline if necessary)
Glute Bridge
Plank
Mountain Climbers
Jumping Jacks
Day 2: 20min Steady State Cardio of choice
Day 3: Bodyweight Circuit
Warm-up: 5-minute light cardio (jog, brisk walk, or jumping jacks)
Circuit (3 rounds, 45 seconds per exercise with 15 seconds rest between exercises):
Reverse Lunges (alternate legs)
Incline Push-ups
Superman
Side Plank (45 seconds per side)
Bicycle Crunches
High Knees
Day 4: 20min Steady State Cardio of choice
Day 5: Bodyweight Circuit
Warm-up: 5-minute light cardio (jog, brisk walk, or jumping jacks)
Circuit (3 rounds, 45 seconds per exercise with 15 seconds rest between exercises):
Step-ups (alternate legs)
Tricep Dips (use parallel bars or a sturdy chair)
Bodyweight Deadlift
Russian Twists
Leg Raises
Butt Kicks"""

BegWeightLossWorkout10 = """Day 1: Full Body Resistance Training
Warm-up: 5-minute light cardio (jog, brisk walk, or jumping jacks)
Goblet Squats: 3 sets of 12-15 reps
Push-ups: 3 sets of 10-12 reps (knees or incline if necessary)
Dumbbell Rows: 3 sets of 12-15 reps
Dumbbell Lunges: 3 sets of 12-15 reps per leg
Plank: 3 sets of 30-60 seconds
Day 2: 20min Steady State Cardio of choice
Day 3: Full Body Resistance Training
Warm-up: 5-minute light cardio (jog, brisk walk, or jumping jacks)
Dumbbell Deadlift: 3 sets of 12-15 reps
Incline Dumbbell Press: 3 sets of 12-15 reps
Seated Dumbbell Shoulder Press: 3 sets of 12-15 reps
Glute Bridge: 3 sets of 12-15 reps
Bicycle Crunches: 3 sets of 15-20 reps
Day 4: 20min Steady State Cardio of choice
Day 5: Full Body Resistance Training
Warm-up: 5-minute light cardio (jog, brisk walk, or jumping jacks)
Step-ups: 3 sets of 12-15 reps per leg
Lat Pulldown: 3 sets of 12-15 reps
Dumbbell Bicep Curls: 3 sets of 12-15 reps
Tricep Dips (use parallel bars or a sturdy chair): 3 sets of 12-15 reps
Leg Raises: 3 sets of 15-20 reps"""


#advanced workouts

#muscle gain
AdvMuscleGainWorkout1 = """Day 1: Push (Chest, Shoulders, Triceps)
Barbell Bench Press: 5 sets of 5 reps
Incline Dumbbell Press: 4 sets of 8-10 reps
Military Press: 4 sets of 8-10 reps
Weighted Dips: 4 sets of 8-10 reps
Close-grip Bench Press: 4 sets of 8-10 reps
Day 2: Pull (Back, Biceps)
Deadlift: 5 sets of 5 reps
Weighted Pull-ups: 4 sets of 8-10 reps
Bent Over Barbell Rows: 4 sets of 8-10 reps
Barbell Curls: 4 sets of 8-10 reps
Hammer Curls: 4 sets of 8-10 reps
Day 3: Legs
Barbell Squats: 5 sets of 5 reps
Romanian Deadlift: 4 sets of 8-10 reps
Leg Press: 4 sets of 8-10 reps
Leg Curls: 4 sets of 10-12 reps
Standing Calf Raises: 4 sets of 10-12 reps
Day 4: Push (Chest, Shoulders, Triceps)
Incline Barbell Bench Press: 5 sets of 5 reps
Dumbbell Bench Press: 4 sets of 8-10 reps
Seated Dumbbell Shoulder Press: 4 sets of 8-10 reps
Cable Tricep Pushdown: 4 sets of 8-10 reps
Skull Crushers: 4 sets of 8-10 reps
Day 5: Pull (Back, Biceps)
Barbell Rows: 5 sets of 5 reps
Weighted Chin-ups: 4 sets of 8-10 reps
T-bar Rows: 4 sets of 8-10 reps
Preacher Curls: 4 sets of 8-10 reps
Concentration Curls: 4 sets of 8-10 reps
Day 6: Legs
Front Squats: 5 sets of 5 reps
Bulgarian Split Squats: 4 sets of 8-10 reps
Leg Extensions: 4 sets of 10-12 reps
Seated Leg Curls: 4 sets of 10-12 reps
Seated Calf Raises: 4 sets of 10-12 reps
Day 7: Rest"""

AdvMuscleGainWorkout2 = """Day 1: Upper Body (Chest, Back, Shoulders, Biceps, Triceps)
Barbell Bench Press: 5 sets of 5 reps
Weighted Pull-ups: 4 sets of 8-10 reps
Seated Dumbbell Shoulder Press: 4 sets of 8-10 reps
Barbell Rows: 4 sets of 8-10 reps
Barbell Curls: 3 sets of 8-10 reps
Skull Crushers: 3 sets of 8-10 reps
Day 2: Lower Body (Legs, Calves, Abs)
Barbell Squats: 5 sets of 5 reps
Romanian Deadlift: 4 sets of 8-10 reps
Leg Press: 4 sets of 8-10 reps
Seated Calf Raises: 4 sets of 10-12 reps
Hanging Leg Raises: 4 sets of 10-15 reps
Day 3: Upper Body (Chest, Back, Shoulders, Biceps, Triceps)
Incline Barbell Bench Press: 5 sets of 5 reps
Weighted Chin-ups: 4 sets of 8-10 reps
Military Press: 4 sets of 8-10 reps
T-bar Rows: 4 sets of 8-10 reps
Hammer Curls: 3 sets of 8-10 reps
Cable Tricep Pushdown: 3 sets of 8-10 reps
Day 4: Lower Body (Legs, Calves, Abs)
Deadlift: 5 sets of 5 reps
Front Squats: 4 sets of 8-10 reps
Leg Curls: 4 sets of 10-12 reps
Standing Calf Raises: 4 sets of 10-12 reps
Cable Crunches: 4 sets of 10-15 reps
Day 5: Push (Chest, Shoulders, Triceps)
Dumbbell Bench Press: 5 sets of 5 reps
Standing Dumbbell Shoulder Press: 4 sets of 8-10 reps
Close-grip Bench Press: 4 sets of 8-10 reps
Cable Fly: 4 sets of 10-12 reps
Dumbbell Lateral Raises: 4 sets of 10-12 reps
Day 6: Pull (Back, Biceps)
Barbell Rows: 5 sets of 5 reps
Weighted Pull-ups: 4 sets of 8-10 reps
Seated Cable Rows: 4 sets of 8-10 reps
Preacher Curls: 4 sets of 8-10 reps
Concentration Curls: 4 sets of 8-10 reps
Day 7: Rest"""

AdvMuscleGainWorkout3 = """Day 1: Upper Body (Chest, Back, Shoulders, Biceps, Triceps)
Barbell Bench Press: 5 sets of 5 reps
Bent Over Barbell Rows: 4 sets of 8-10 reps
Seated Dumbbell Shoulder Press: 4 sets of 8-10 reps
Weighted Pull-ups: 4 sets of 8-10 reps
Alternating Dumbbell Curls: 3 sets of 8-10 reps
Cable Tricep Pushdown: 3 sets of 8-10 reps
Day 2: Lower Body (Legs, Calves, Abs)
Barbell Squats: 5 sets of 5 reps
Leg Press: 4 sets of 8-10 reps
Romanian Deadlift: 4 sets of 8-10 reps
Standing Calf Raises: 4 sets of 10-12 reps
Ab Wheel Rollout: 4 sets of 10-15 reps
Day 3: Rest
Day 4: Push (Chest, Shoulders, Triceps)
Incline Dumbbell Bench Press: 5 sets of 5 reps
Military Press: 4 sets of 8-10 reps
Weighted Dips: 4 sets of 8-10 reps
Cable Fly: 4 sets of 10-12 reps
Lateral Raises: 4 sets of 10-12 reps
Day 5: Pull (Back, Biceps)
Deadlift: 5 sets of 5 reps
Weighted Chin-ups: 4 sets of 8-10 reps
T-bar Rows: 4 sets of 8-10 reps
Hammer Curls: 4 sets of 8-10 reps
Incline Dumbbell Curls: 4 sets of 8-10 reps
Day 6: Legs (Quads, Hamstrings, Calves, Abs)
Front Squats: 5 sets of 5 reps
Bulgarian Split Squats: 4 sets of 8-10 reps
Leg Curls: 4 sets of 10-12 reps
Seated Calf Raises: 4 sets of 10-12 reps
Plank: 3 sets of 60 seconds
Day 7: Rest"""

AdvMuscleGainWorkout4 = """Day 1: Chest
Barbell Bench Press: 5 sets of 5 reps
Incline Dumbbell Press: 4 sets of 8-10 reps
Decline Barbell Bench Press: 4 sets of 8-10 reps
Chest Fly: 4 sets of 10-12 reps
Day 2: Back
Deadlift: 5 sets of 5 reps
Weighted Pull-ups: 4 sets of 8-10 reps
Bent Over Rows: 4 sets of 8-10 reps
Seated Cable Rows: 4 sets of 10-12 reps
Day 3: Shoulders
Military Press: 5 sets of 5 reps
Dumbbell Lateral Raises: 4 sets of 8-10 reps
Face Pulls: 4 sets of 10-12 reps
Arnold Press: 4 sets of 8-10 reps
Day 4: Arms
Barbell Curls: 5 sets of 5 reps
Close-grip Bench Press: 5 sets of 5 reps
Hammer Curls: 4 sets of 8-10 reps
Cable Tricep Pushdown: 4 sets of 8-10 reps
Day 5: Legs
Barbell Squats: 5 sets of 5 reps
Romanian Deadlift: 4 sets of 8-10 reps
Leg Press: 4 sets of 8-10 reps
Leg Curls: 4 sets of 10-12 reps
Day 6: Rest
Day 7: Rest"""

AdvMuscleGainWorkout5 = """Day 1: Chest and Triceps
Barbell Bench Press: 5 sets of 5 reps
Incline Dumbbell Press: 4 sets of 8-10 reps
Decline Push-ups: 4 sets of 10-12 reps
Skull Crushers: 4 sets of 8-10 reps
Cable Tricep Pushdown: 3 sets of 8-10 reps
Day 2: Back and Biceps
Deadlift: 5 sets of 5 reps
Weighted Pull-ups: 4 sets of 8-10 reps
Seated Cable Rows: 4 sets of 8-10 reps
Barbell Curls: 4 sets of 8-10 reps
Hammer Curls: 3 sets of 8-10 reps
Day 3: Legs and Shoulders
Barbell Squats: 5 sets of 5 reps
Leg Press: 4 sets of 8-10 reps
Romanian Deadlift: 4 sets of 8-10 reps
Seated Dumbbell Shoulder Press: 4 sets of 8-10 reps
Dumbbell Lateral Raises: 3 sets of 10-12 reps
Day 4: Chest and Triceps
Incline Barbell Bench Press: 5 sets of 5 reps
Chest Fly: 4 sets of 10-12 reps
Close-grip Bench Press: 4 sets of 8-10 reps
Overhead Tricep Extension: 4 sets of 8-10 reps
Dips: 3 sets of 10-12 reps
Day 5: Back and Biceps
Bent Over Rows: 5 sets of 5 reps
Weighted Chin-ups: 4 sets of 8-10 reps
T-bar Rows: 4 sets of 8-10 reps
Concentration Curls: 4 sets of 8-10 reps
Incline Dumbbell Curls: 3 sets of 8-10 reps
Day 6: Legs and Shoulders
Front Squats: 5 sets of 5 reps
Bulgarian Split Squats: 4 sets of 8-10 reps
Leg Curls: 4 sets of 10-12 reps
Military Press: 4 sets of 8-10 reps
Face Pulls: 3 sets of 10-12 reps
Day 7: Rest"""

AdvMuscleGainWorkout6 = """Day 1: Push (Chest, Shoulders, Triceps)
Barbell Bench Press: 5 sets of 5 reps
Incline Dumbbell Press: 4 sets of 8-10 reps
Military Press: 4 sets of 8-10 reps
Close-grip Bench Press: 4 sets of 8-10 reps
Dumbbell Lateral Raises: 3 sets of 10-12 reps
Day 2: Pull (Back, Biceps)
Deadlift: 5 sets of 5 reps
Weighted Pull-ups: 4 sets of 8-10 reps
Seated Cable Rows: 4 sets of 8-10 reps
Barbell Curls: 4 sets of 8-10 reps
Hammer Curls: 3 sets of 8-10 reps
Day 3: Legs (Quads, Hamstrings, Calves)
Barbell Squats: 5 sets of 5 reps
Romanian Deadlift: 4 sets of 8-10 reps
Leg Press: 4 sets of 8-10 reps
Leg Curls: 4 sets of 10-12 reps
Standing Calf Raises: 3 sets of 12-15 reps
Day 4: Upper Body (Chest, Back, Shoulders, Biceps, Triceps)
Incline Barbell Bench Press: 5 sets of 5 reps
Bent Over Rows: 4 sets of 8-10 reps
Seated Dumbbell Shoulder Press: 4 sets of 8-10 reps
Concentration Curls: 4 sets of 8-10 reps
Cable Tricep Pushdown: 3 sets of 8-10 reps
Day 5: Lower Body (Legs, Calves, Abs)
Front Squats: 5 sets of 5 reps
Bulgarian Split Squats: 4 sets of 8-10 reps
Seated Leg Curls: 4 sets of 10-12 reps
Seated Calf Raises: 3 sets of 12-15 reps
Hanging Leg Raises: 4 sets of 10-15 reps
Day 6: Rest
Day 7: Rest"""

AdvMuscleGainWorkout7 = """Day 1: Upper Body (Chest, Back, Shoulders, Biceps, Triceps)
Barbell Bench Press: 5 sets of 5 reps
Bent Over Rows: 4 sets of 8-10 reps
Seated Dumbbell Shoulder Press: 4 sets of 8-10 reps
Barbell Curls: 4 sets of 8-10 reps
Cable Tricep Pushdown: 3 sets of 8-10 reps
Day 2: Lower Body (Legs, Calves, Abs)
Barbell Squats: 5 sets of 5 reps
Romanian Deadlift: 4 sets of 8-10 reps
Leg Press: 4 sets of 8-10 reps
Standing Calf Raises: 3 sets of 12-15 reps
Hanging Leg Raises: 4 sets of 10-15 reps
Day 3: Rest
Day 4: Push (Chest, Shoulders, Triceps)
Incline Barbell Bench Press: 5 sets of 5 reps
Military Press: 4 sets of 8-10 reps
Close-grip Bench Press: 4 sets of 8-10 reps
Dumbbell Lateral Raises: 3 sets of 10-12 reps
Overhead Tricep Extension: 3 sets of 8-10 reps
Day 5: Pull (Back, Biceps)
Deadlift: 5 sets of 5 reps
Weighted Pull-ups: 4 sets of 8-10 reps
Seated Cable Rows: 4 sets of 8-10 reps
Hammer Curls: 4 sets of 8-10 reps
Preacher Curls: 3 sets of 8-10 reps
Day 6: Legs (Quads, Hamstrings, Calves)
Front Squats: 5 sets of 5 reps
Bulgarian Split Squats: 4 sets of 8-10 reps
Leg Curls: 4 sets of 10-12 reps
Seated Calf Raises: 3 sets of 12-15 reps
Plank: 3 sets of 60 seconds
Day 7: Rest"""

AdvMuscleGainWorkout8 = """Day 1: Chest and Back
Barbell Bench Press: 5 sets of 5 reps
Weighted Pull-ups: 4 sets of 8-10 reps
Incline Dumbbell Press: 4 sets of 8-10 reps
T-bar Rows: 4 sets of 8-10 reps
Chest Fly: 3 sets of 10-12 reps
Day 2: Arms and Shoulders
Military Press: 5 sets of 5 reps
Barbell Curls: 4 sets of 8-10 reps
Skull Crushers: 4 sets of 8-10 reps
Dumbbell Lateral Raises: 3 sets of 10-12 reps
Hammer Curls: 3 sets of 8-10 reps
Day 3: Legs
Barbell Squats: 5 sets of 5 reps
Romanian Deadlift: 4 sets of 8-10 reps
Leg Press: 4 sets of 8-10 reps
Leg Curls: 4 sets of 10-12 reps
Standing Calf Raises: 3 sets of 12-15 reps
Day 4: Rest
Day 5: Upper Body (Chest, Back, Shoulders, Biceps, Triceps)
Incline Barbell Bench Press: 5 sets of 5 reps
Bent Over Rows: 4 sets of 8-10 reps
Seated Dumbbell Shoulder Press: 4 sets of 8-10 reps
Concentration Curls: 4 sets of 8-10 reps
Cable Tricep Pushdown: 3 sets of 8-10 reps
Day 6: Lower Body (Legs, Calves, Abs)
Front Squats: 5 sets of 5 reps
Bulgarian Split Squats: 4 sets of 8-10 reps
Seated Leg Curls: 4 sets of 10-12 reps
Seated Calf Raises: 3 sets of 12-15 reps
Hanging Leg Raises: 4 sets of 10-15 reps
Day 7: Rest"""

AdvMuscleGainWorkout9 = """Day 1: Push (Chest, Shoulders, Triceps)
Barbell Bench Press: 5 sets of 5 reps
Incline Dumbbell Press: 4 sets of 8-10 reps
Seated Dumbbell Shoulder Press: 4 sets of 8-10 reps
Close-grip Bench Press: 4 sets of 8-10 reps
Dumbbell Lateral Raises: 3 sets of 10-12 reps
Day 2: Pull (Back, Biceps)
Deadlift: 5 sets of 5 reps
Weighted Pull-ups: 4 sets of 8-10 reps
Seated Cable Rows: 4 sets of 8-10 reps
Preacher Curls: 4 sets of 8-10 reps
Hammer Curls: 3 sets of 8-10 reps
Day 3: Legs (Quads, Hamstrings, Calves)
Barbell Squats: 5 sets of 5 reps
Romanian Deadlift: 4 sets of 8-10 reps
Leg Press: 4 sets of 8-10 reps
Leg Curls: 4 sets of 10-12 reps
Standing Calf Raises: 3 sets of 12-15 reps
Day 4: Rest
Day 5: Upper Body (Chest, Back, Shoulders, Biceps, Triceps)
Incline Barbell Bench Press: 5 sets of 5 reps
Bent Over Rows: 4 sets of 8-10 reps
Military Press: 4 sets of 8-10 reps
Barbell Curls: 4 sets of 8-10 reps
Cable Tricep Pushdown: 3 sets of 8-10 reps
Day 6: Lower Body (Legs, Calves, Abs)
Front Squats: 5 sets of 5 reps
Bulgarian Split Squats: 4 sets of 8-10 reps
Leg Curls: 4 sets of 10-12 reps
Seated Calf Raises: 3 sets of 12-15 reps
Hanging Leg Raises: 4 sets of 10-15 reps
Day 7: Rest"""

AdvMuscleGainWorkout10 = """Day 1: Chest and Triceps
Barbell Bench Press: 5 sets of 5 reps
Incline Dumbbell Press: 4 sets of 8-10 reps
Chest Fly: 4 sets of 10-12 reps
Close-grip Bench Press: 4 sets of 8-10 reps
Cable Tricep Pushdown: 3 sets of 8-10 reps
Day 2: Back and Biceps
Deadlift: 5 sets of 5 reps
Weighted Pull-ups: 4 sets of 8-10 reps
Bent Over Rows: 4 sets of 8-10 reps
Barbell Curls: 4 sets of 8-10 reps
Hammer Curls: 3 sets of 8-10 reps
Day 3: Legs and Shoulders
Barbell Squats: 5 sets of 5 reps
Romanian Deadlift: 4 sets of 8-10 reps
Leg Press: 4 sets of 8-10 reps
Seated Dumbbell Shoulder Press: 4 sets of 8-10 reps
Dumbbell Lateral Raises: 3 sets of 10-12 reps
Day 4: Rest
Day 5: Push (Chest, Shoulders, Triceps)
Incline Barbell Bench Press: 5 sets of 5 reps
Military Press: 4 sets of 8-10 reps
Dumbbell Fly: 4 sets of 10-12 reps
Skull Crushers: 4 sets of 8-10 reps
Overhead Tricep Extension: 3 sets of 8-10 reps
Day 6: Pull (Back, Biceps)
Barbell Rows: 5 sets of 5 reps
Weighted Chin-ups: 4 sets of 8-10 reps
Seated Cable Rows: 4 sets of 8-10 reps
Preacher Curls: 4 sets of 8-10 reps
Concentration Curls: 3 sets of 8-10 reps
Day 7: Legs (Quads, Hamstrings, Calves)
Front Squats: 5 sets of 5 reps
Bulgarian Split Squats: 4 sets of 8-10 reps
Leg Curls: 4 sets of 10-12 reps
Standing Calf Raises: 3 sets of 12-15 reps
Seated Calf Raises: 3 sets of 12-15 reps"""

#weight loss
AdvWeightLossWorkout1 = """Day 1: Upper Body Strength Training
Barbell Bench Press: 4 sets of 8-10 reps
Pull-ups: 4 sets of 8-10 reps (use assistance if necessary)
Seated Dumbbell Shoulder Press: 4 sets of 8-10 reps
Barbell Bent Over Rows: 4 sets of 8-10 reps
EZ-Bar Skull Crushers: 3 sets of 10-12 reps
Barbell Bicep Curls: 3 sets of 10-12 reps
Day 2: Lower Body Strength Training
Barbell Squats: 4 sets of 8-10 reps
Romanian Deadlift: 4 sets of 8-10 reps
Leg Press: 4 sets of 10-12 reps
Seated Leg Curls: 4 sets of 10-12 reps
Calf Raises: 4 sets of 15-20 reps
Day 3: HIIT (High-Intensity Interval Training)
Choose one of the following exercises: sprints, jump rope, burpees, or mountain climbers
Perform 10-12 rounds of 20-30 seconds of high-intensity work followed by 10-20 seconds of rest
Day 4: Active Rest
30-45 minutes of light to moderate-intensity cardio (jogging, cycling, or brisk walking)
Stretching and mobility work
Day 5: Full Body Strength Training
Deadlift: 4 sets of 6-8 reps
Weighted Chin-ups: 4 sets of 8-10 reps
Incline Barbell Bench Press: 4 sets of 8-10 reps
Leg Press: 4 sets of 10-12 reps
Hanging Leg Raises: 3 sets of 12-15 reps
Day 6: HIIT (High-Intensity Interval Training)
Choose one of the following exercises: sprints, jump rope, burpees, or mountain climbers
Perform 10-12 rounds of 20-30 seconds of high-intensity work followed by 10-20 seconds of rest
Day 7: Rest"""

AdvWeightLossWorkout2 = """Day 1: Upper Body Strength Training
Barbell Bench Press: 4 sets of 6-8 reps
Weighted Pull-ups: 4 sets of 6-8 reps
Standing Military Press: 4 sets of 6-8 reps
T-Bar Row: 4 sets of 8-10 reps
Dips: 3 sets of 10-12 reps
Hammer Curls: 3 sets of 10-12 reps
Day 2: Lower Body Strength Training
Front Squats: 4 sets of 6-8 reps
Barbell Lunges: 4 sets of 8-10 reps per leg
Leg Extensions: 3 sets of 10-12 reps
Lying Leg Curls: 3 sets of 10-12 reps
Seated Calf Raises: 4 sets of 15-20 reps
Day 3: Circuit Training
Circuit (4 rounds, 45 seconds per exercise with 15 seconds rest between exercises):
Kettlebell Swings
Box Jumps
Push-ups
Jumping Lunges
TRX Rows
Bicycle Crunches
Day 4: Active Rest
30-45 minutes of light to moderate-intensity cardio (jogging, cycling, or brisk walking)
Stretching and mobility work
Day 5: Full Body Strength Training
Sumo Deadlift: 4 sets of 6-8 reps
Incline Dumbbell Bench Press: 4 sets of 8-10 reps
Weighted Chin-ups: 4 sets of 6-8 reps
Bulgarian Split Squats: 4 sets of 8-10 reps per leg
Toes-to-Bar: 3 sets of 12-15 reps
Day 6: Cardio
40-45 minutes of steady-state moderate-intensity cardio (jogging, cycling, or brisk walking)
Day 7: Rest"""

AdvWeightLossWorkout3 = """Day 1: Upper Body Strength Training
Close-Grip Bench Press: 4 sets of 6-8 reps
Weighted Chin-ups: 4 sets of 6-8 reps
Arnold Press: 4 sets of 8-10 reps
Pendlay Rows: 4 sets of 8-10 reps
Overhead Tricep Extension: 3 sets of 10-12 reps
Concentration Curls: 3 sets of 10-12 reps
Day 2: Lower Body Strength Training
Box Squats: 4 sets of 6-8 reps
Single-Leg Romanian Deadlift: 4 sets of 8-10 reps per leg
Leg Extensions: 3 sets of 10-12 reps
Seated Leg Curls: 3 sets of 10-12 reps
Standing Calf Raises: 4 sets of 15-20 reps
Day 3: Plyometrics
Perform 4 rounds of the following exercises, with 30-45 seconds rest between exercises:
Box Jumps: 8-10 reps
Plyometric Push-ups: 8-10 reps
Lateral Bounds: 8-10 reps per side
Plyometric Lunges: 8-10 reps per leg
Day 4: Active Rest
30-45 minutes of light to moderate-intensity cardio (jogging, cycling, or brisk walking)
Stretching and mobility work
Day 5: Full Body Strength Training
Hex Bar Deadlift: 4 sets of 6-8 reps
Dumbbell Flat Bench Press: 4 sets of 8-10 reps
Weighted Pull-ups: 4 sets of 6-8 reps
Rear Foot Elevated Split Squats: 4 sets of 8-10 reps per leg
Hanging Knee Raises: 3 sets of 12-15 reps
Day 6: Cardio
40-45 minutes of steady-state moderate-intensity cardio (jogging, cycling, or brisk walking)
Day 7: Rest"""

AdvWeightLossWorkout4 = """Day 1: Upper Body Strength Training
Decline Barbell Bench Press: 4 sets of 6-8 reps
Weighted Wide-Grip Pull-ups: 4 sets of 6-8 reps
Upright Rows: 4 sets of 8-10 reps
Seated Cable Rows: 4 sets of 8-10 reps
Skull Crushers: 3 sets of 10-12 reps
Preacher Curls: 3 sets of 10-12 reps
Day 2: Lower Body Strength Training
Paused Squats: 4 sets of 6-8 reps
Step-Ups: 4 sets of 8-10 reps per leg
Leg Press: 3 sets of 10-12 reps
Seated Leg Curls: 3 sets of 10-12 reps
Donkey Calf Raises: 4 sets of 15-20 reps
Day 3: High-Intensity Interval Training (HIIT)
Perform 6-8 rounds of the following exercises, with 20 seconds of work followed by 10 seconds of rest:
Burpees
Mountain Climbers
Jump Squats
High Knees
Day 4: Active Rest
30-45 minutes of light to moderate-intensity cardio (jogging, cycling, or brisk walking)
Stretching and mobility work
Day 5: Full Body Strength Training
Trap Bar Deadlift: 4 sets of 6-8 reps
Push-ups: 4 sets of 8-10 reps
Bent Over Rows: 4 sets of 8-10 reps
Goblet Squats: 4 sets of 8-10 reps
Russian Twists: 3 sets of 12-15 reps
Day 6: Cardio
40-45 minutes of steady-state moderate-intensity cardio (jogging, cycling, or brisk walking)
Day 7: Rest"""

AdvWeightLossWorkout5 = """Day 1: Upper Body Strength Training
Incline Dumbbell Bench Press: 4 sets of 6-8 reps
T-Bar Rows: 4 sets of 6-8 reps
Lateral Raises: 4 sets of 8-10 reps
Face Pulls: 4 sets of 8-10 reps
Cable Tricep Pushdowns: 3 sets of 10-12 reps
Hammer Curls: 3 sets of 10-12 reps
Day 2: Lower Body Strength Training
Front Squats: 4 sets of 6-8 reps
Bulgarian Split Squats: 4 sets of 8-10 reps per leg
Hack Squats: 3 sets of 10-12 reps
Lying Leg Curls: 3 sets of 10-12 reps
Seated Calf Raises: 4 sets of 15-20 reps
Day 3: High-Intensity Interval Training (HIIT)
Perform 6-8 rounds of the following exercises, with 20 seconds of work followed by 10 seconds of rest:
Jumping Lunges
Push-up Jacks
Tuck Jumps
Plank Jacks
Day 4: Active Rest
30-45 minutes of light to moderate-intensity cardio (jogging, cycling, or brisk walking)
Stretching and mobility work
Day 5: Full Body Strength Training
Sumo Deadlift: 4 sets of 6-8 reps
Standing Military Press: 4 sets of 8-10 reps
Chin-ups: 4 sets of 8-10 reps
Lunges: 4 sets of 8-10 reps per leg
Planks: 3 sets of 60-second holds
Day 6: Cardio
40-45 minutes of steady-state moderate-intensity cardio (jogging, cycling, or brisk walking)
Day 7: Rest"""

AdvWeightLossWorkout6 = """Day 1: Upper Body Strength Training
Dumbbell Bench Press: 4 sets of 6-8 reps
Bent Over Dumbbell Rows: 4 sets of 6-8 reps
Arnold Press: 4 sets of 8-10 reps
Cable Flyes: 4 sets of 8-10 reps
Overhead Tricep Extension: 3 sets of 10-12 reps
Concentration Curls: 3 sets of 10-12 reps
Day 2: Lower Body Strength Training
Box Squats: 4 sets of 6-8 reps
Romanian Deadlifts: 4 sets of 8-10 reps
Leg Extensions: 3 sets of 10-12 reps
Seated Leg Curls: 3 sets of 10-12 reps
Standing Calf Raises: 4 sets of 15-20 reps
Day 3: High-Intensity Interval Training (HIIT)
Perform 6-8 rounds of the following exercises, with 20 seconds of work followed by 10 seconds of rest:
Box Jumps
Plank to Push-up
Skater Jumps
Bicycle Crunches
Day 4: Active Rest
30-45 minutes of light to moderate-intensity cardio (jogging, cycling, or brisk walking)
Stretching and mobility work
Day 5: Full Body Strength Training
Trap Bar Deadlift: 4 sets of 6-8 reps
Incline Push-ups: 4 sets of 8-10 reps
Lat Pulldowns: 4 sets of 8-10 reps
Dumbbell Step-ups: 4 sets of 8-10 reps per leg
Hanging Leg Raises: 3 sets of 12-15 reps
Day 6: Cardio
40-45 minutes of steady-state moderate-intensity cardio (jogging, cycling, or brisk walking)
Day 7: Rest"""

AdvWeightLossWorkout7 = """Day 1: Upper Body Strength Training
Push-ups: 4 sets of 10-15 reps
Pull-ups: 4 sets of 6-8 reps
Dumbbell Shoulder Press: 4 sets of 8-10 reps
Cable Rows: 4 sets of 8-10 reps
Skull Crushers: 3 sets of 10-12 reps
Zottman Curls: 3 sets of 10-12 reps
Day 2: Lower Body Strength Training
Goblet Squats: 4 sets of 6-8 reps
Single-Leg Deadlifts: 4 sets of 8-10 reps per leg
Leg Press: 3 sets of 10-12 reps
Glute Bridges: 3 sets of 10-12 reps
Farmer's Walk: 3 sets of 45-second carries
Day 3: High-Intensity Interval Training (HIIT)
Perform 6-8 rounds of the following exercises, with 20 seconds of work followed by 10 seconds of rest:
Mountain Climbers
Burpees
High Knees
Russian Twists
Day 4: Active Rest
30-45 minutes of light to moderate-intensity cardio (jogging, cycling, or brisk walking)
Stretching and mobility work
Day 5: Full Body Strength Training
Deadlift: 4 sets of 6-8 reps
Dips: 4 sets of 8-10 reps
Seated Cable Rows: 4 sets of 8-10 reps
Walking Lunges: 4 sets of 8-10 reps per leg
V-Ups: 3 sets of 12-15 reps
Day 6: Cardio
40-45 minutes of steady-state moderate-intensity cardio (jogging, cycling, or brisk walking)
Day 7: Rest"""

AdvWeightLossWorkout8 = """Day 1: Upper Body Strength Training
Barbell Bench Press: 4 sets of 6-8 reps
Pendlay Rows: 4 sets of 6-8 reps
Dumbbell Lateral Raises: 4 sets of 8-10 reps
Cable Tricep Pushdowns: 4 sets of 8-10 reps
Hammer Curls: 3 sets of 10-12 reps
Plank: 3 sets of 45-60 seconds
Day 2: Lower Body Strength Training
Front Squats: 4 sets of 6-8 reps
Bulgarian Split Squats: 4 sets of 8-10 reps per leg
Leg Curls: 3 sets of 10-12 reps
Seated Calf Raises: 3 sets of 10-12 reps
Ab Wheel Rollouts: 3 sets of 10-12 reps
Day 3: High-Intensity Interval Training (HIIT)
Perform 6-8 rounds of the following exercises, with 20 seconds of work followed by 10 seconds of rest:
Jump Squats
Push-up to Plank Jacks
Speed Skaters
Reverse Crunches
Day 4: Active Rest
30-45 minutes of light to moderate-intensity cardio (jogging, cycling, or brisk walking)
Stretching and mobility work
Day 5: Full Body Strength Training
Barbell Clean and Press: 4 sets of 6-8 reps
Chin-ups: 4 sets of 8-10 reps
Push-ups with Shoulder Taps: 4 sets of 8-10 reps
Dumbbell Reverse Lunges: 4 sets of 8-10 reps per leg
Russian Twists: 3 sets of 12-15 reps
Day 6: Cardio
40-45 minutes of steady-state moderate-intensity cardio (jogging, cycling, or brisk walking)
Day 7: Rest"""

AdvWeightLossWorkout9 = """Day 1: Upper Body Strength Training
Incline Dumbbell Bench Press: 4 sets of 6-8 reps
T-Bar Rows: 4 sets of 6-8 reps
Seated Dumbbell Shoulder Press: 4 sets of 8-10 reps
Close-Grip Bench Press: 4 sets of 8-10 reps
EZ-Bar Curls: 3 sets of 10-12 reps
Hanging Leg Raises: 3 sets of 12-15 reps
Day 2: Lower Body Strength Training
Barbell Squats: 4 sets of 6-8 reps
Romanian Deadlifts: 4 sets of 8-10 reps
Leg Extensions: 3 sets of 10-12 reps
Standing Calf Raises: 3 sets of 10-12 reps
Bicycle Crunches: 3 sets of 12-15 reps
Day 3: High-Intensity Interval Training (HIIT)
Perform 6-8 rounds of the following exercises, with 20 seconds of work followed by 10 seconds of rest:
Box Jumps
Spiderman Push-ups
Lateral Bounds
Flutter Kicks
Day 4: Active Rest
30-45 minutes of light to moderate-intensity cardio (jogging, cycling, or brisk walking)
Stretching and mobility work
Day 5: Full Body Strength Training
Barbell Rows: 4 sets of 6-8 reps
Weighted Dips: 4 sets of 8-10 reps
Kettlebell Swings: 4 sets of 8-10 reps
Step-Ups: 4 sets of 8-10 reps per leg
Plank with Shoulder Taps: 3 sets of 30-45 seconds
Day 6: Cardio
40-45 minutes of steady-state moderate-intensity cardio (jogging, cycling, or brisk walking)
Day 7: Rest"""

AdvWeightLossWorkout10 = """Day 1: Upper Body Strength Training
Standing Military Press: 4 sets of 6-8 reps
Pull-ups: 4 sets of 6-8 reps
Dumbbell Chest Fly: 4 sets of 8-10 reps
Skull Crushers: 4 sets of 8-10 reps
Concentration Curls: 3 sets of 10-12 reps
Russian Twists: 3 sets of 15-20 reps
Day 2: Lower Body Strength Training
Hack Squats: 4 sets of 6-8 reps
Glute Bridge: 4 sets of 8-10 reps
Leg Press: 3 sets of 10-12 reps
Farmer's Walk: 3 sets of 30-45 seconds
V-ups: 3 sets of 12-15 reps
Day 3: High-Intensity Interval Training (HIIT)
Perform 6-8 rounds of the following exercises, with 20 seconds of work followed by 10 seconds of rest:
Burpees
Mountain Climbers
Split Jumps
V-sit Crunches
Day 4: Active Rest
30-45 minutes of light to moderate-intensity cardio (jogging, cycling, or brisk walking)
Stretching and mobility work
Day 5: Full Body Strength Training
Deadlifts: 4 sets of 6-8 reps
Incline Push-ups: 4 sets of 8-10 reps
Kettlebell Goblet Squats: 4 sets of 8-10 reps
Single Leg Romanian Deadlifts: 4 sets of 8-10 reps per leg
Plank Jacks: 3 sets of 30-45 seconds
Day 6: Cardio
40-45 minutes of steady-state moderate-intensity cardio (jogging, cycling, or brisk walking)
Day 7: Rest"""
# Connect to the SQLite database
conn = sqlite3.connect("workouts.db")

# Create a workouts table
conn.execute("""
CREATE TABLE IF NOT EXISTS workout_plans (
    workout_id INTEGER PRIMARY KEY,
    workout_description TEXT,
    fitness_goal TEXT
)
""")

# Insert 10 workout programs for muscle gain for beginners (fitness_goal: "beg_muscle_gain")
beginner_muscle_gain_workouts = [
    (1, BegMuscleGainWorkout1, "beg_muscle_gain"),
    (2, BegMuscleGainWorkout2, "beg_muscle_gain"),
    (3, BegMuscleGainWorkout3, "beg_muscle_gain"),
    (4, BegMuscleGainWorkout4, "beg_muscle_gain"),
    (5, BegMuscleGainWorkout5, "beg_muscle_gain"),
    (6, BegMuscleGainWorkout6, "beg_muscle_gain"),
    (7, BegMuscleGainWorkout7, "beg_muscle_gain"),
    (8, BegMuscleGainWorkout8, "beg_muscle_gain"),
    (9, BegMuscleGainWorkout9, "beg_muscle_gain"),
    (10, BegMuscleGainWorkout10, "beg_muscle_gain")
]

# Insert 10 workout programs for muscle gain for advanced individuals (fitness_goal: "muscle_gain")
advanced_muscle_gain_workouts = [
    (11, AdvMuscleGainWorkout1, "adv_muscle_gain"),
    (12, AdvMuscleGainWorkout2, "adv_muscle_gain"),
    (13, AdvMuscleGainWorkout3, "adv_muscle_gain"),
    (14, AdvMuscleGainWorkout4, "adv_muscle_gain"),
    (15, AdvMuscleGainWorkout5, "adv_muscle_gain"),
    (16, AdvMuscleGainWorkout6, "adv_muscle_gain"),
    (17, AdvMuscleGainWorkout7, "adv_muscle_gain"),
    (18, AdvMuscleGainWorkout8, "adv_muscle_gain"),
    (19, AdvMuscleGainWorkout9, "adv_muscle_gain"),
    (20, AdvMuscleGainWorkout10, "adv_muscle_gain")
]

# Insert 10 workout programs for weight loss for beginners (fitness_goal: "beg_weight_loss")
beginner_weight_loss_workouts = [
    (21, BegWeightLossWorkout1, "beg_weight_loss"),
    (22, BegWeightLossWorkout2, "beg_weight_loss"),
    (23, BegWeightLossWorkout3, "beg_weight_loss"),
    (24, BegWeightLossWorkout4, "beg_weight_loss"),
    (25, BegWeightLossWorkout5, "beg_weight_loss"),
    (26, BegWeightLossWorkout6, "beg_weight_loss"),
    (27, BegWeightLossWorkout7, "beg_weight_loss"),
    (28, BegWeightLossWorkout8, "beg_weight_loss"),
    (29, BegWeightLossWorkout9, "beg_weight_loss"),
    (30, BegWeightLossWorkout10, "beg_weight_loss")
]

# Insert 10 workout programs for weight loss for advanced individuals (fitness_goal: "beg_weight_loss")
advanced_weight_loss_workouts = [
    (31, AdvWeightLossWorkout1, "adv_weight_loss"),
    (32, AdvWeightLossWorkout2, "adv_weight_loss"),
    (33, AdvWeightLossWorkout3, "adv_weight_loss"),
    (34, AdvWeightLossWorkout4, "adv_weight_loss"),
    (35, AdvWeightLossWorkout5, "adv_weight_loss"),
    (36, AdvWeightLossWorkout6, "adv_weight_loss"),
    (37, AdvWeightLossWorkout7, "adv_weight_loss"),
    (38, AdvWeightLossWorkout8, "adv_weight_loss"),
    (39, AdvWeightLossWorkout9, "adv_weight_loss"),
    (40, AdvWeightLossWorkout10, "adv_weight_loss")
]



# Add the workout programs to the database
conn.executemany("INSERT INTO workout_plans VALUES (?, ?, ?)", beginner_muscle_gain_workouts)
conn.executemany("INSERT INTO workout_plans VALUES (?, ?, ?)", advanced_muscle_gain_workouts)

conn.executemany("INSERT INTO workout_plans VALUES (?, ?, ?)", beginner_weight_loss_workouts)
conn.executemany("INSERT INTO workout_plans VALUES (?, ?, ?)", advanced_weight_loss_workouts)
conn.commit()

# Close the database connection
conn.close()