# IncodeVision Internship - Task 2
# Project: To-Do List App (Console Based)

tasks = []


def add_task():
    task_name = input("\nEnter your new task: ").strip()

    if task_name == "":
        print("Task cannot be empty!")
        return

    task = {
        "name": task_name,
        "completed": False
    }

    tasks.append(task)
    print(f"Task '{task_name}' added successfully!")


def view_tasks():
    print("\n========== YOUR TO-DO LIST ==========")

    if not tasks:
        print("Your to-do list is empty!")
        return

    for index, task in enumerate(tasks, start=1):
        if task["completed"]:
            status = "Completed"
            symbol = "✓"
        else:
            status = "Pending"
            symbol = " "

        print(f"{index}. [{symbol}] {task['name']} - {status}")

    completed_count = sum(
        1 for task in tasks if task["completed"]
    )

    print("-------------------------------------")
    print(f"Total tasks: {len(tasks)}")
    print(f"Completed: {completed_count}")
    print(f"Pending: {len(tasks) - completed_count}")


def complete_task():
    view_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("\nEnter task number to complete: "))

        if 1 <= task_number <= len(tasks):
            task = tasks[task_number - 1]

            if task["completed"]:
                print("This task is already completed!")
            else:
                task["completed"] = True
                print(f"'{task['name']}' marked as completed!")
        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number!")


def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        task_number = int(input("\nEnter task number to delete: "))

        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"'{removed_task['name']}' deleted successfully!")
        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number!")


def main():
    while True:
        print("\n=====================================")
        print("       MY TO-DO LIST MANAGER")
        print("=====================================")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("5. Exit")
        print("=====================================")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("\nThank you for using My To-Do List Manager!")
            print("Keep organizing, keep achieving!")
            break
        else:
            print("Invalid choice! Please select from 1 to 5.")


if __name__ == "__main__":
    main()