# ===== Importing libraries ============
from datetime import datetime  # Import for handling and formatting dates

# ===== Login Section =====
# Load usernames and passwords from user.txt
users = {}  # Dictionary to store username-password pairs

# Open the user file in read mode to load users and passwords
with open("user.txt", "r") as file:
    for line in file:
        username, password = line.strip().split(", ")  # Split line into username and password
        users[username] = password  # Add to users dictionary

# Repeated login prompt until valid credentials are entered
while True:
    username_input = input("Enter username: ")

    # Check if username exists
    if username_input not in users:
        print("❌ Username not found. Please try again.\n")
        continue  # Ask again if not found

    password_input = input("Enter password: ")

    # Check if the entered password is correct
    if users[username_input] != password_input:
        print("❌ Incorrect password. Please try again.\n")
    else:
        print(f"\n✅ Login successful. Welcome, {username_input}!\n")
        break  # Exit loop on successful login

# ===== Main Menu =====
while True:
    # Display current loaded users for debugging purposes
    print("Users loaded:", users)

    # Display menu options and convert input to lowercase
    menu = input('''\nPlease select one of the following options:
r  - Register a new user
a  - Add a task
va - View all tasks
vm - View my tasks
e  - Exit
: ''').lower()

    if menu == 'r':
        # ===== Register a new user =====
        new_user = input("Enter a new username: ")

        # Warn if the username already exists
        if new_user in users:
            print("⚠️ Username already exists. Choose a different one.")
            continue

        new_pass = input("Enter a new password: ")
        confirm_pass = input("Confirm your password: ")

        # Ensure password confirmation matches before registering
        if new_pass == confirm_pass:
            with open("user.txt", "a") as file:
                file.write(f"{new_user}, {new_pass}\n")
            print("✅ User registered successfully.")
        else:
            print("❌ Passwords do not match. Try again.")

    elif menu == 'a':
        # ===== Add a new task =====
        assigned_to = input("Enter the username to assign the task to: ").strip()

        # Ensure assigned user exists
        if assigned_to not in users:
            print("❌ User does not exist. Please try again.")
            continue

        title = input("Enter the task title: ")
        description = input("Enter the task description: ")
        due_date = input("Enter the task due date (YYYY-MM-DD): ")
        date_assigned = datetime.today().strftime("%d %b %Y")  # Format today's date as string
        complete = 'No'  # New tasks are not yet completed

        # Save the new task to tasks.txt
        with open("tasks.txt", "a") as task_file:
            task_file.write(
                f"{assigned_to}, {title}, {description}, "
                f"{date_assigned}, {due_date}, {complete}\n"
            )

        print("✅ Task added successfully.")

    elif menu == 'va':
        # ===== View all tasks =====
        try:
            with open("tasks.txt", "r") as task_file:
                tasks = task_file.readlines()

                # Inform if there are no tasks
                if not tasks:
                    print("📭 No tasks available.\n")
                else:
                    print("\n=== All Tasks ===")
                    # Loop over each task and print formatted output
                    for task in tasks:
                        (user, title, description,
                         date_assigned, due_date, completed) = task.strip().split(", ")

                        print(f'''
------------------------------
Task Title     : {title}
Assigned To    : {user}
Date Assigned  : {date_assigned}
Due Date       : {due_date}
Completed?     : {completed}
Description    : {description}
------------------------------
''')
        except FileNotFoundError:
            print("⚠️ No tasks file found. Please add a task first.")

    elif menu == 'vm':
        # ===== View tasks assigned to the logged-in user =====
        print(f"\n📋 Tasks for {username_input}:")

        try:
            with open("tasks.txt", "r") as task_file:
                tasks = task_file.readlines()
                found = False  # Track if user has any tasks

                # Print only tasks assigned to the current user
                for task in tasks:
                    (user, title, description,
                     date_assigned, due_date, completed) = task.strip().split(", ")

                    if user == username_input:
                        found = True
                        print(f'''
------------------------------
Task Title     : {title}
Assigned To    : {user}
Date Assigned  : {date_assigned}
Due Date       : {due_date}
Completed?     : {completed}
Description    : {description}
------------------------------
''')
                if not found:
                    print("📭 You have no tasks assigned.\n")

        except FileNotFoundError:
            print("⚠️ No tasks file found. Please add a task first.")

    elif menu == 'e':
        # ===== Exit the program =====
        print("👋 Goodbye!")
        break  # Exit the main loop to terminate the program

    else:
        # ===== Handle invalid menu input =====
        print("❗ Invalid option. Please select from the menu.")
