# ===== Importing libraries ============
from datetime import datetime

# ===== Login Section =====
# Load usernames and passwords from user.txt
users = {}
with open("user.txt", "r") as file:
    for line in file:
        username, password = line.strip().split(", ")
        users[username] = password

# Repeated login prompt until valid credentials are entered
while True:
    username_input = input("Enter username: ")

    if username_input not in users:
        print("❌ Username not found. Please try again.\n")
        continue

    password_input = input("Enter password: ")

    if users[username_input] != password_input:
        print("❌ Incorrect password. Please try again.\n")
    else:
        print(f"\n✅ Login successful. Welcome, {username_input}!\n")
        break

# ===== Main Menu =====
while True:
    # Displaying menu options
    print("Users loaded:", users)
    menu = input('''\nPlease select one of the following options:
r  - Register a new user
a  - Add a task
da - Display all tasks
vm - View my tasks
e  - Exit
: ''').lower()

    if menu == 'r':
        # ===== Register a new user =====
        new_user = input("Enter a new username: ")

        if new_user in users:
            print("⚠️ Username already exists. Choose a different one.")
            continue

        new_pass = input("Enter a new password: ")
        confirm_pass = input("Confirm your password: ")

        if new_pass == confirm_pass:
            with open("user.txt", "a") as file:
                file.write(f"{new_user}, {new_pass}\n")
            print("✅ User registered successfully.")
        else:
            print("❌ Passwords do not match. Try again.")

    elif menu == 'a':
        # ===== Add a new task =====
        assigned_to = input("Enter the username to assign the task to: ").strip()

        if assigned_to not in users:
            print("❌ User does not exist. Please try again.")
            continue

        title = input("Enter the task title: ")
        description = input("Enter the task description: ")
        due_date = input("Enter the task due date (YYYY-MM-DD): ")
        date_assigned = datetime.today().strftime("%d %b %Y")
        complete = 'No'

        with open("tasks.txt", "a") as task_file:
            task_file.write(
                f"{assigned_to}, {title}, {description}, "
                f"{date_assigned}, {due_date}, {complete}\n"
            )

        print("✅ Task added successfully.")

    elif menu == 'da':
        # ===== View all tasks =====
        try:
            with open("tasks.txt", "r") as task_file:
                tasks = task_file.readlines()

                if not tasks:
                    print("📭 No tasks available.\n")
                else:
                    print("\n=== All Tasks ===")
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
                found = False

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
        break

    else:
        # ===== Handle invalid menu input =====
        print("❗ Invalid option. Please select from the menu.")
