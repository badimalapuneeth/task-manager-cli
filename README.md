# Python CLI Task Manager

## Project Description

A simple command-line task management application built using Python. It allows users to add tasks, view existing tasks, and exit the application through an interactive menu.

## Features

- Add a new task with a title and description.
- Automatically generate a unique numeric task ID.
- Assign `pending` status to new tasks.
- View all available tasks.
- Display a friendly message when no tasks are available.
- Reject empty or whitespace-only task titles.
- Handle invalid menu choices without crashing.
- Exit the application cleanly.

## Technologies Used

- Python 3.12+
- uv
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
├── .gitignore
├── .python-version
├── LEARNINGS.md
├── README.md
├── pyproject.toml
└── uv.lock
```

## Task Storage

Tasks are stored in a Python list while the application is running. Each task contains:

- ID
- Title
- Description
- Status

New tasks receive the default status `pending`.

**Note:** Tasks are not permanently saved after the application exits.

## Author

Badimala Puneeth
