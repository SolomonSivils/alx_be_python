# personal daily reminder
# prompt for task description, priority, and time_bound
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower() 
time_bound = input("Is it time-bound? (yes/no): ").lower() 

# init  reminder message
reminder = ""

# process the task based on priority and time sensitivity using a match-case statement
match priority:
    case "high":
        if time_bound == "yes":
            reminder= f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
        else:
            reminder= f"Reminder: '{task}' is a high priority task." 
    case "medium":
        if time_bound == "yes":
            reminder  = f"Reminder: '{task}' is a medium priority task, endeavor to create time."
        else:
            reminder  = f"Reminder: '{task}' is a medium priority task." 
    case "low":
        if time_bound == "yes":
            reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
        else:
            reminder = f"Note: '{task}' is a low priority task."
    case _: 
        reminder = f"Note: '{task}' has incorrect priority '{priority}'. Please input one of the following priority (high/medium/low)."

print(reminder)