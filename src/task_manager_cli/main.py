# Store all tasks in this list
tasks = []

# Generate unique task IDs
next_task_id = 1


def add_task():
    global next_task_id

    # Get task details from the user
    title = input("Enter task title: ").strip()

    # Validate the title
    if not title:
        print("Error: Task title cannot be empty.")
        return

    description = input("Enter task description: ").strip()
    # Create a task dictionary
    task = {
        "id": next_task_id,
        "title": title,
        "description": description,
        "status": "pending",
    }

    # Store the task in the list
    tasks.append(task)

    # Display success message
    print(f"Task #{next_task_id} created successfully!")

    # Increase ID for the next task
    next_task_id += 1


def view_tasks():

    # Check whether the task list is empty
    if not tasks:
        print("\nNo tasks available. Please add a task first.")
        return

    print("\n========== YOUR TASKS ==========")

    # Loop through all tasks
    for task in tasks:
        print(f"\nTask ID: {task['id']}")
        print(f"Title: {task['title']}")
        print(f"Description: {task['description']}")
        print(f"Status: {task['status']}")
        print("--------------------------------")


def main():
    try:
        while True:
            print("\n========== TASK MANAGER ==========")
            print("1. Add task")
            print("2. View tasks")
            print("3. Exit")

            choice = input("Choose an option: ").strip()

            if choice == "1":
                add_task()

            elif choice == "2":
                view_tasks()

            elif choice == "3":
                print("Goodbye!")
                break

            else:
                print("Invalid option! Please choose 1, 2 or 3.")

    except KeyboardInterrupt:
        print("\nProgram interrupted. Goodbye!")


if __name__ == "__main__":
    main()
