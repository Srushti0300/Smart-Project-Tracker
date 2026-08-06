tasks = []

while True:
    print("\n===== Smart Project Tracker =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("✅ Task added successfully!")

    elif choice == "2":
        print("\n📋 Your Tasks:")
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            print("\n📋 Your Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            delete = int(input("Enter task number to delete: "))

            if 1 <= delete <= len(tasks):
                removed_task = tasks.pop(delete - 1)
                print(f"✅ '{removed_task}' deleted successfully!")
            else:
                print("❌ Invalid task number.")

    elif choice == "4":
        print("👋 Thank you for using Smart Project Tracker!")
        break

    else:
        print("❌ Invalid choice! Please try again.")