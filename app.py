from flask import Flask, request, render_template
import sqlite3
from datetime import datetime

app = Flask(__name__)
DB_NAME = "honeypot.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS login_attempts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip_address TEXT,
            username TEXT,
            password TEXT,
            user_agent TEXT,
            headers TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO login_attempts (ip_address, username, password, user_agent, headers, timestamp) VALUES (?, ?, ?, ?, ?, ?)",
            (
                request.remote_addr,
                request.form.get("username"),
                request.form.get("password"),
                request.headers.get("User-Agent"),
                str(dict(request.headers)),
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
        )
        conn.commit()
        conn.close()
        return render_template("login.html", error="Invalid username or password")
    return render_template("login.html")

@app.route("/admin/logs")
def admin_logs():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM login_attempts ORDER BY id DESC")
    logs = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM login_attempts")
    total = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(DISTINCT ip_address) FROM login_attempts")
    unique_ips = cursor.fetchone()[0]
    last_time = logs[0][6] if logs else "N/A"
    conn.close()
    return render_template("admin.html", logs=logs, total=total, unique_ips=unique_ips, last_time=last_time)

if __name__ == "__main__":
    app.run(debug=True)

