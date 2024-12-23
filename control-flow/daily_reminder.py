def get_valid_input(prompt, valid_options):
    """Prompt the user until a valid input is provided."""
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_options:
            return user_input
        print(f"Invalid input. Please enter one of the following: {', '.join(valid_options)}")

def main():
    
    task = input("Enter your task: ").strip()
    priority = get_valid_input("Priority (high/medium/low): ", ["high", "medium", "low"])
    time_bound = get_valid_input("Is it time-bound? (yes/no): ", ["yes", "no"])

    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task."
        case "medium":
            reminder = f"'{task}' is a medium priority task."
        case "low":
            reminder = f"'{task}' is a low priority task."

    if time_bound == "yes":
        reminder += " It requires immediate attention today!"
    else:
        reminder += " Consider completing it when you have free time."

    print("\nReminder:", reminder)

if __name__ == "__main__":
    main()

