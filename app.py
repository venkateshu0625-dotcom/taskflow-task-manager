from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from pathlib import Path

app = Flask(__name__)
app.secret_key = "change-this-to-a-random-secret-before-deploying"
BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / "tasks.db"


def get_db_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    with get_db_connection() as connection:
        connection.execute(
            """CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                completed INTEGER NOT NULL DEFAULT 0,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            )"""
        )


@app.route("/")
def index():
    status = request.args.get("status", "all")
    connection = get_db_connection()

    if status == "active":
        tasks = connection.execute(
            "SELECT * FROM tasks WHERE completed = 0 ORDER BY id DESC"
        ).fetchall()
    elif status == "completed":
        tasks = connection.execute(
            "SELECT * FROM tasks WHERE completed = 1 ORDER BY id DESC"
        ).fetchall()
    else:
        status = "all"
        tasks = connection.execute(
            "SELECT * FROM tasks ORDER BY id DESC"
        ).fetchall()

    totals = connection.execute(
        "SELECT COUNT(*) AS total, "
        "COALESCE(SUM(CASE WHEN completed = 0 THEN 1 ELSE 0 END), 0) AS active, "
        "COALESCE(SUM(CASE WHEN completed = 1 THEN 1 ELSE 0 END), 0) AS completed "
        "FROM tasks"
    ).fetchone()
    connection.close()
    return render_template("index.html", tasks=tasks, status=status, totals=totals)


@app.post("/add")
def add_task():
    title = request.form.get("title", "").strip()
    if not title:
        flash("Please enter a task before adding it.", "error")
    elif len(title) > 200:
        flash("Tasks must be 200 characters or fewer.", "error")
    else:
        with get_db_connection() as connection:
            connection.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
        flash("Task added successfully.", "success")
    return redirect(url_for("index"))


@app.post("/toggle/<int:task_id>")
def toggle_task(task_id):
    with get_db_connection() as connection:
        connection.execute(
            "UPDATE tasks SET completed = CASE completed WHEN 0 THEN 1 ELSE 0 END WHERE id = ?",
            (task_id,),
        )
    return redirect(url_for("index", status=request.form.get("status", "all")))


@app.post("/delete/<int:task_id>")
def delete_task(task_id):
    with get_db_connection() as connection:
        connection.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    flash("Task deleted.", "success")
    return redirect(url_for("index", status=request.form.get("status", "all")))


@app.post("/clear-completed")
def clear_completed():
    with get_db_connection() as connection:
        connection.execute("DELETE FROM tasks WHERE completed = 1")
    flash("Completed tasks cleared.", "success")
    return redirect(url_for("index"))


init_db()

if __name__ == "__main__":
    app.run(debug=True)
