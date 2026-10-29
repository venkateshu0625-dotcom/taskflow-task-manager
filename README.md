# TaskFlow — Task Manager Web App

TaskFlow is a responsive task management web application built with Python, Flask, SQLite, HTML, and CSS. It helps users keep a lightweight to-do list, track completed work, and filter tasks by status.

## Features

- Create tasks with input validation
- Mark tasks as completed or active
- Delete individual tasks
- Filter all, active, and completed tasks
- View task summary counts
- Clear all completed tasks
- Persist tasks in a local SQLite database
- Responsive layout for desktop and mobile

## Tech stack

- Python 3
- Flask
- SQLite
- HTML5 and CSS3

## Run locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/taskflow-task-manager.git
cd taskflow-task-manager
```

Or download the ZIP and extract it.

### 2. Create and activate a virtual environment

Windows Command Prompt:

```bat
python -m venv .venv
.venv\Scripts\activate
```

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

If `python` is not recognized, try replacing `python` with `py`.

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Start the app

```bash
python app.py
```

Open http://127.0.0.1:5000 in your browser. The SQLite database (`tasks.db`) is created automatically the first time the app starts.

## Project structure

```text
taskflow-task-manager/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Notes

- This is a learning and portfolio project intended for local use.
- Before deploying publicly, replace the development secret key with a securely generated environment variable, disable Flask debug mode, and add CSRF protection and production hosting configuration.
- Google Fonts are loaded from an external CDN; the layout remains usable if that request fails.

## Possible improvements

- User accounts and authentication
- Due dates and priority levels
- Search tasks
- Automated tests
- Deployment to a hosting platform

## Author

Add your name and GitHub profile here.
