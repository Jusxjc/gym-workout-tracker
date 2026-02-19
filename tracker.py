import json
def add_workout(): # Ask the user to enter a workout
    exercise= input("Enter an exercise: ")
    sets= int(input("Enter sets: "))
    reps= int(input("Enter reps: "))
    weight= (input("Enter weight (or bodyweight): "))
    return (exercise,sets,reps,weight)

def output_workout_added(exercise,sets,reps,weight): # Print the new workout added
    print("Workout added:")
    print("Exercise:", exercise)
    print("Sets:", sets)
    print("Reps:", reps)
    print("Weight:", weight)
      
def create_workout_dict(exercise,sets,reps,weight): # Adds the new workout to a list of workouts via dictionary
    workout_input= {"Exercise": exercise,
            "Sets": sets,
            "Reps": reps,
            "Weight": weight
            }
    return (workout_input)

def get_workout_list(workout_input): # Reads the JSON file and adds all workouts to a list
    try:
        with open("workouts.json","r") as f:
            json_data= json.load(f)
            json_data.append(workout_input)
            return json_data
    except FileNotFoundError:
         print("File not found")
         return [] # Returns an empty list to prevent errors when updating workout list
    except:
         print("An error occurred not relating to file found")
         return []

def update_workout_list(workouts): # Updates the stored workouts in the JSON file
    try:
        with open("workouts.json","w") as f:
                json.dump(workouts,f, indent=4)
    except FileNotFoundError:
         print ("File not found error")
    except:
         print("An error occurred")
    


def main(): #Main 
      print("Welcome to Gym tracker")
      exercise,sets,reps,weight= add_workout()
      output_workout_added(exercise,sets,reps,weight)
      workout_input= create_workout_dict(exercise,sets,reps,weight)
      workouts = get_workout_list(workout_input)
      update_workout_list(workouts)
      


main()