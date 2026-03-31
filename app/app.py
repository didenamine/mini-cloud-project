from flask import Flask, request, jsonify
import mysql.connector
import redis
import os
import time
import socket
app = Flask(__name__)

# MySQL config
def connect_db():
    while True:
        try:
            db = mysql.connector.connect(
                host="db",
                user="admin",
                password="admin",
                database="tasks"
            )
            print("✅ Connected to MySQL")
            return db
        except Exception as e:
            print("⏳ Waiting for MySQL...", e)
            time.sleep(3)

db = connect_db()
cursor = db.cursor()

# Redis
cache = redis.Redis(host='redis', port=6379)

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255)
)
""")
@app.route("/")
def home():
    return f"Hello from {socket.gethostname()}"

@app.route("/tasks", methods=["GET"])
def get_tasks():
    # Cache check
    cached = cache.get("tasks")
    if cached:
        return cached

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    result = [{"id": t[0], "title": t[1]} for t in tasks]

    cache.set("tasks", str(result))
    return jsonify(result)

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.json
    cursor.execute("INSERT INTO tasks (title) VALUES (%s)", (data["title"],))
    db.commit()

    cache.delete("tasks")

    return {"message": "Task added"}

@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    cursor.execute("DELETE FROM tasks WHERE id=%s", (id,))
    db.commit()

    cache.delete("tasks")

    return {"message": "Task deleted"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
