# daily_reminder.py

# Prompt for a single task
task = input("Enter your task for the day: ")
priority = input("Enter the priority level (high, medium, low): ").lower()
time_bound = input("Is the task time-sensitive? (yes or no): ").lower()

# Process the task based on priority
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high-priority task."
    case "medium":
        message = f"Reminder: '{task}' is a medium-priority task."
    case "low":
        message = f"Reminder: '{task}' is a low-priority task."
    case _:
        message = f"Reminder: '{task}' has an unspecified priority."

# Modify the reminder based on time sensitivity
if time_bound == "yes":
    message += " This task requires immediate attention today!"

# Print the customized reminder
print(message)
