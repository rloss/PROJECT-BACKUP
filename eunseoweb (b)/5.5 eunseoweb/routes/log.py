from flask import Blueprint, render_template, request, redirect
import sqlite3
from datetime import datetime
import os

log_bp = Blueprint('log', __name__)
DB_PATH = os.path.join("data", "log.db")

@log_bp.route("/log", methods=["GET", "POST"])
def log():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        created_at = datetime.now().strftime("%Y.%m.%d %H:%M")

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO logs (title, content, created_at) VALUES (?, ?, ?)",
            (title, content, created_at)
        )
        conn.commit()
        conn.close()

        return redirect("/log")

    # GET 요청: 로그 조회
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT title, content, created_at FROM logs ORDER BY created_at DESC")
    logs = [
        {"title": row[0], "content": row[1], "date": row[2]}
        for row in cursor.fetchall()
    ]
    conn.close()

    return render_template("log.html", logs=logs)
