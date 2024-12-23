task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case 'high':
        reminder = f"Reminder: '{task}' is a high priority task"
        if time_bound == 'yes':
            reminder += " that requires immediate attention today!"
        else:
            reminder += " that can be done later, but should be prioritized."
    case 'medium':
        reminder = f"Reminder: '{task}' is a medium priority task"
        if time_bound == 'yes':
            reminder += " and requires attention soon."
        else:
            reminder += " and can be scheduled for later."
    case 'low':
        reminder = f"Reminder: '{task}' is a low priority task"
        if time_bound == 'yes':
            reminder += " but doesn't require immediate action."
        else:
            reminder += " Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority entered. Please enter high, medium, or low."

print(reminder)
