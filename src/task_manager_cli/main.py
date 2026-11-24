import json
from pathlib import Path

DATA_FILE = Path("tasks.json")


def load_tasks():
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError:
        print("Warning: tasks.json contains invalid JSON.")
        return []


def save_tasks():
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


tasks = load_tasks()

next_task_id = max((task["id"] for task in tasks), default=0) + 1


def add_task():
    global next_task_id

    title = input("Enter task title: ").strip()

    if not title:
        print("Error: Task title cannot be empty.")
        return

    description = input("Enter task description: ").strip()

    task = {
        "id": next_task_id,
        "title": title,
        "description": description,
        "status": "pending",
    }

    tasks.append(task)
    save_tasks()

    print(f"Task #{next_task_id} created successfully!")

    next_task_id += 1


def view_tasks():

    if not tasks:
        print("\nNo tasks available. Please add a task first.")
        return

    print("\n========== YOUR TASKS ==========")

    for task in tasks:
        print(f"\nTask ID: {task['id']}")
        print(f"Title: {task['title']}")
        print(f"Description: {task['description']}")
        print(f"Status: {task['status']}")
        print("--------------------------------")


def mark_task_completed():

    if not tasks:
        print("\nNo tasks available. Please add a task first.")
        return

    try:
        task_id = int(input("Enter task ID to mark as completed: "))

    except ValueError:
        print("Invalid input! Please enter a numeric task ID.")
        return

    for task in tasks:
        if task["id"] == task_id:

            if task["status"] == "completed":
                print("This task is already completed.")
                return

            task["status"] = "completed"
            save_tasks()
            print(f"Task #{task_id} marked as completed!")
            return

    print(f"Task ID {task_id} not found.")


def delete_task():

    if not tasks:
        print("\nNo tasks available to delete.")
        return

    try:
        task_id = int(input("Enter task ID to delete: "))

    except ValueError:
        print("Invalid input! Please enter a numeric task ID.")
        return

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks()
            print(f"Task #{task_id} deleted successfully!")
            return

    print(f"Task ID {task_id} not found.")


def main():
    try:
        while True:
            print("\n========== TASK MANAGER ==========")
            print("1. Add task")
            print("2. View tasks")
            print("3. Mark task as completed")
            print("4. Delete task")
            print("5.Exit")

            choice = input("Choose an option: ").strip()

            if choice == "1":
                add_task()

            elif choice == "2":
                view_tasks()

            elif choice == "3":
                mark_task_completed()

            elif choice == "4":
                delete_task()

            elif choice == "5":
                print("GoodBye!")
                break

            else:
                print("Invalid option! Please choose 1, 2, 3, 4 or 5.")

    except KeyboardInterrupt:
        print("\nProgram interrupted. Goodbye!")


if __name__ == "__main__":
    main()
