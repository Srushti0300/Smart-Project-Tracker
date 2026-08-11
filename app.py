import json

try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []


while True:
    print("\n===== Smart Project Tracker =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Show Progress")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")

        print("\nSelect Priority:")
        print("1. High")
        print("2. Medium")
        print("3. Low")

        priority_choice = input("Enter priority: ")

        if priority_choice == "1":
            priority = "High"
        elif priority_choice == "2":
            priority = "Medium"
        elif priority_choice == "3":
            priority = "Low"
        else:
            priority = "Medium"

        tasks.append({
            "name": task,
            "status": "Pending",
            "priority": priority
        })

        print("✅ Task added successfully!")

    elif choice == "2":
        print("\n📋 Your Tasks:")

        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(
                    f"{i}. {task['name']} | "
                    f"Priority: {task['priority']} | "
                    f"Status: {task['status']}"
                )

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['name']} - {task['status']}")

            number = int(input("Enter task number to complete: "))

            if 1 <= number <= len(tasks):
                tasks[number - 1]["status"] = "Completed"
                print("✅ Task completed!")
            else:
                print("❌ Invalid task number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task['name']}")

            number = int(input("Enter task number to delete: "))

            if 1 <= number <= len(tasks):
                removed = tasks.pop(number - 1)
                print(f"✅ '{removed['name']}' deleted!")
            else:
                print("❌ Invalid task number.")

    elif choice == "5":
        total = len(tasks)
        completed = sum(
            1 for task in tasks
            if task["status"] == "Completed"
        )

        pending = total - completed

        print("\n📊 Project Progress")
        print("Total Tasks:", total)
        print("Completed:", completed)
        print("Pending:", pending)

        if total > 0:
            progress = (completed / total) * 100
            print("Progress:", round(progress, 1), "%")
        else:
            print("Progress: 0%")

    elif choice == "6":
        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)

        print("💾 Tasks saved successfully!")
        print("👋 Thank you!")
        break

    else:
        print("❌ Invalid choice!")