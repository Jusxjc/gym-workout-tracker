import json

exercise= input("Enter an exercise: ")
sets= int(input("Enter sets: "))
reps= int(input("Enter reps: "))
weight= (input("Enter weight (or bodyweight): "))

print("Workout added:")
print("Exercise:", exercise)
print("Sets:", sets)
print("Reps:", reps)
print("Weight:", weight)
workouts= []
workout_input= {"Exercise": exercise,
          "Sets": sets,
          "Reps": reps,
          "Weight": sets
          }
with open("workouts.json","r") as f:
    json_data= json.load(f)
    workouts.extend(json_data)
    workouts.append(workout_input)

    print(workouts)



with open("workouts.json","w") as f:
        json.dump(workouts,f, indent=4)
