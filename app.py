tasks = []

while True:
    print("\n===== Smart Project Tracker =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append({
            "name": task,
            "status": "Pending"
        })
        print("✅ Task added successfully!")

    elif choice == "2":
        print("\n📋 Your Tasks:")
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['name']} - {task['status']}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\n📋 Your Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['name']} - {task['status']}")

            number = int(input("Enter task number to complete: "))

            if 1 <= number <= len(tasks):
                tasks[number - 1]["status"] = "Completed"
                print("✅ Task marked as completed!")
            else:
                print("❌ Invalid task number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\n📋 Your Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['name']} - {task['status']}")

            delete = int(input("Enter task number to delete: "))

            if 1 <= delete <= len(tasks):
                removed = tasks.pop(delete - 1)
                print(f"✅ '{removed['name']}' deleted successfully!")
            else:
                print("❌ Invalid task number.")

    elif choice == "5":
        print("👋 Thank you for using Smart Project Tracker!")
        break

    else:
        print("❌ Invalid choice! Please try again.")