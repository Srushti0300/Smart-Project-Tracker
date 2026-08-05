tasks = []

while True:
    print("\n----- Smart Project Tracker -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        print("\nYour Tasks:")
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for task in tasks:
                print("-", task)

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")