# Python CLI Task Manager

## Project Description

A simple command-line task management application built using Python. It allows users to add tasks, view existing tasks, and exit the application through an interactive menu.

## Features

- Add a new task with a title and description.
- Automatically generate a unique numeric task ID.
- Assign `pending` status to new tasks.
- View all available tasks.
- Display a friendly message when no tasks are available.
- Reject empty task titles.
- Handle invalid menu choices.
- Exit the application cleanly.

## Technologies Used

- Python 3.12+
- uv
- Git

## Project Setup

1. Clone or download the project.
2. Open the project folder in the terminal.
3. Install the project dependencies:

```bash
uv sync
```

## Run the Application

```bash
uv run python -m task_manager_cli.main
```

## Application Menu

```text
========== TASK MANAGER ==========
1. Add task
2. View tasks
3. Exit
Choose an option:
```

## Project Structure

```text
task-manager-cli/
├── src/
│   └── task_manager_cli/
│       ├── __init__.py
│       └── main.py
├── README.md
├── LEARNINGS.md
├── pyproject.toml
└── uv.lock
```

## Author

Badimala Puneeth
