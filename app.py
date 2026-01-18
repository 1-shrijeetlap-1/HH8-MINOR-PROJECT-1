from flask import Flask, request, render_template, redirect, url_for, session
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = "honeypot_secret_key"
DB_NAME = "honeypot.db"
ADMIN_KEY = "admin123"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
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
        c = conn.cursor()
        c.execute(
            "INSERT INTO login_attempts VALUES (NULL,?,?,?,?,?,?)",
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

@app.route("/admin", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        if request.form.get("admin_key") == ADMIN_KEY:
            session["admin"] = True
            return redirect(url_for("admin_logs"))
        else:
            return render_template("admin_login.html", error="Invalid admin key")
    return render_template("admin_login.html")

@app.route("/admin/logs")
def admin_logs():
    if not session.get("admin"):
        return redirect(url_for("admin_login"))

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM login_attempts ORDER BY id DESC")
    logs = c.fetchall()

    c.execute("SELECT COUNT(*) FROM login_attempts")
    total = c.fetchone()[0]

    c.execute("SELECT COUNT(DISTINCT ip_address) FROM login_attempts")
    unique_ips = c.fetchone()[0]

    last_time = logs[0][6] if logs else "N/A"
    conn.close()

    return render_template("admin.html", logs=logs, total=total, unique_ips=unique_ips, last_time=last_time)

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
