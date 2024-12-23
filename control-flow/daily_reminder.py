def main():
    print("Welcome to your Daily Reminder Program!")

    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    if priority not in ("high", "medium", "low"):
        print("Invalid priority level. Please restart and enter 'high', 'medium', or 'low'.")
        return
    if time_bound not in ("yes", "no"):
        print("Invalid input for time-bound. Please restart and enter 'yes' or 'no'.")
        return

    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"

    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        reminder += ". Consider completing it when you have free time."

print(f"\nReminder: {reminder}")


if __name__ == "__main__":
    main()

