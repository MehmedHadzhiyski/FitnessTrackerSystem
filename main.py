# Personal Fitness Tracker System 🏋️‍♂️

# Collections to store fitness data
workouts = {}  # To store workout types and durations
calories = []  # To store calorie intake for meals


def log_workout(workout_type: str, duration: float):
    if duration > 0:
        workouts[workout_type.lower()] = duration
        print(f"Successfully logged workout type {workout_type.lower()} with a duration of "
              f"{duration} minutes to your workout data.")
    else:
        print("Error: Invalid workout minutes.")


def log_calorie_intake(calories_consumed: float):
    if calories_consumed > 0:
        calories.append(calories_consumed)
        print(f"Successfully logged {calories_consumed} calories to your calories data.")
    else:
        print("Error: Invalid calories.")


def view_progress():
    total_workout_time = sum(workouts.values())
    total_calories = sum(calories)
    print(f"Your total workout time is {total_workout_time} minutes and your total calories - {total_calories} cal.")

    if total_workout_time == 0 or total_calories == 0:
        if total_workout_time == 0:
            print("Don't give on your workout goals! You've got this!")
        if total_calories == 0:
            print("Start eating some carbs and protein foods! They are essential for your body and workout!")
    else:
        print(f"Nice job, you're doing very well! Keep up the momentum!")


def reset_progress():
    workouts.clear()
    calories.clear()
    print(f"Successfully cleared workout and calorie data.")


def set_daily_goals(workout_minutes: float, calorie_limit: float) -> tuple[int, int] | tuple[float, float]:
    if workout_minutes <= 0 or calorie_limit <= 0:
        if workout_minutes <= 0:
            print("Error: Invalid workout minutes.")
        if calorie_limit <= 0:
            print("Error: Invalid calorie limit.")
        return 0, 0
    print(f"Successfully set workout goal to {workout_minutes} minutes and calorie goal to {calorie_limit} cal.")
    return workout_minutes, calorie_limit


def encouragement_system(workout_goal, calorie_goal):
    total_workout_time = sum(workouts.values())
    total_calories = sum(calories)

    if total_workout_time >= workout_goal > 0:
        print(f"Congratulations! You have managed to achieve your workout goal!"
              f"\nWorkout goal: {workout_goal} min."
              f"\nYour total workout time: {total_workout_time} min.")
    elif not workout_goal:
        print(f"You do not have a workout goal.")
    else:
        diff = workout_goal - total_workout_time
        print(f"Sorry. You haven't reached your workout goal. You need {diff} more minutes to complete the goal."
              f"\nWorkout goal: {workout_goal} min."
              f"\nYour total workout time: {total_workout_time} min.")

    print()

    if total_calories >= calorie_goal > 0:
        print(f"Congratulations! You have managed to achieve your calorie goal!"
              f"\nCalorie goal: {calorie_goal} cal."
              f"\nYour total calories consumed: {total_calories} cal.")
    elif not calorie_goal:
        print("You do not have a calorie goal.")
    else:
        diff = calorie_goal - total_calories
        print(f"Sorry. You haven't reached your calorie goal. You need {diff} more calories to complete the goal."
              f"\nCalorie goal: {calorie_goal} cal."
              f"\nYour total calories consumed: {total_calories} cal.")


def main():
    """Main function to interact with the user."""
    # Variables for daily goals
    workout_goal = 0  # Daily workout goal in minutes
    calorie_goal = 0  # Daily calorie intake goal

    print("Welcome to the Personal Fitness Tracker System 🏋️‍♂️\n")

    while True:
        # Display menu options
        print("1. Log Workout")
        print("2. Log Calorie Intake")
        print("3. View Progress")
        print("4. Reset Progress")
        print("5. Set Daily Goals")
        print("6. Check goal progress")
        print("7. Exit")

        # Prompt user for their choice
        choice = input("\nEnter your choice: ")

        if choice == '1':
            # Prompt for workout type and duration
            workout_type = input("Enter your workout type: ")
            duration = float(input("Enter a duration in minutes: "))
            log_workout(workout_type, duration)

        elif choice == '2':
            # Prompt for calories consumed
            calories_consumed = float(input("Enter your consumed calories: "))
            log_calorie_intake(calories_consumed)

        elif choice == '3':
            # Call view_progress function
            view_progress()

        elif choice == '4':
            # Call reset_progress function
            reset_progress()

        elif choice == '5':
            # Prompt for daily goals
            workout_minutes = float(input("Enter an amount of workout minutes: "))
            calorie_limit = float(input("Enter a calorie amount: "))
            workout_goal, calorie_goal = set_daily_goals(workout_minutes, calorie_limit)

        elif choice == '6':
            # Call encouragement_system function
            encouragement_system(workout_goal, calorie_goal)

        elif choice == '7':
            # Print a goodbye message and break the loop
            print("Thank you for using the Fitness Tracker. Stay healthy! 💪")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
