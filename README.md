# Python CLI Task Manager

## Project Description

A command-line task management application built using Python. It allows users to add, view, mark tasks as completed, and delete tasks through an interactive menu.

The application uses JSON file storage to save tasks permanently, so task data remains available even after restarting the application.

## Features

- Add tasks with a title and description.
- Automatically generate unique numeric task IDs.
- Assign `pending` status to new tasks.
- View all available tasks.
- Mark tasks as completed.
- Delete tasks using their IDs.
- Reject empty or whitespace-only task titles.
- Handle invalid user input.
- Display friendly messages when no tasks are available.
- Save tasks permanently using JSON.
- Load previously saved tasks when the application starts.
- Handle missing or invalid JSON files.
- Exit the application cleanly.

## Technologies Used

- Python 3.12+
- uv
- pytest
- JSON
- Git

## Prerequisites

Before running this project, install:

- Python 3.12 or newer
- Git
- uv
- Visual Studio Code or another code editor

Verify the installations:

```powershell
python --version
git --version
uv --version
```

## Project Setup

1. Clone or download the project.
2. Open the project folder in the terminal.
3. Install the project dependencies:

```bash
uv sync
```

## Run the Application

Execute the following command from the project directory:

```bash
uv run python -m task_manager_cli.main
```

## Application Menu

```text
========== TASK MANAGER ==========
1. Add task
2. View tasks
3. Mark task as completed
4. Delete task
5. Exit
Choose an option:
```

## Project Structure

```text
task-manager-cli/
│
├── src/
│   └── task_manager_cli/
│       ├── __init__.py
│       └── main.py
│
├── tests/
│   └── test_main.py
│
├── tasks.json
├── .gitignore
├── .python-version
├── LEARNINGS.md
├── README.md
├── pyproject.toml
└── uv.lock
```

## Task Storage

Tasks are stored permanently in a JSON file named `tasks.json`.

Each task contains:

- ID
- Title
- Description
- Status

New tasks receive the default status `pending`.

The application automatically loads previously saved tasks when it starts and saves changes whenever a task is added, completed, or deleted.

If the JSON file does not exist, the application starts with an empty task list. It also handles invalid JSON data gracefully.

## Running Automated Tests

This project uses pytest for automated testing.

Run all tests using:

```powershell
uv run pytest -v
```

The tests cover:

- Adding tasks.
- Adding multiple tasks.
- Marking tasks as completed.
- Handling already completed tasks.
- Deleting tasks.
- Handling invalid task IDs.
- Handling non-existing tasks.
- Rejecting blank task titles.
- Handling an empty task list.
- Saving tasks to JSON.
- Loading tasks from JSON.
- Handling invalid JSON.
- Handling missing JSON files.

## Author

Badimala Puneeth
