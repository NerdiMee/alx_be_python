def main():
    print("Welcome to your Daily Reminder Program!")

    while True:
        task = input("Enter your task: ").strip()
        if task:
            break
        print("Task cannot be empty. Please enter a valid task.")

    while True:
        priority = input("Priority (high/medium/low): ").strip().lower()
        if priority in ("high", "medium", "low"):
            break
        print("Invalid priority level. Please enter 'high', 'medium', or 'low'.")

    while True:
        time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
        if time_bound in ("yes", "no"):
            break
        print("Invalid input for time-bound. Please enter 'yes' or 'no'.")

    if time_bound == "yes":
        print(f"\nReminder: '{task}' is a {priority} priority task that requires immediate attention today!")
    else:
        print(f"\nReminder: '{task}' is a {priority} priority task. Consider completing it when you have free time.")

if __name__ == "__main__":
    main()
