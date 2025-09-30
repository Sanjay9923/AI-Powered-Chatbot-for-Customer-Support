from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

# Ensure database file exists in project folder
DB_PATH = os.path.join(os.path.dirname(__file__), "chatbot.db")

# Connect to SQLite database
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS faq (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL
)
""")
conn.commit()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_text = request.form["msg"]

    # Search for a matching question
    cursor.execute("SELECT answer FROM faq WHERE question LIKE ?", ('%' + user_text + '%',))
    result = cursor.fetchone()

    if result:
        return result[0]
    else:
        return "Sorry, I don't understand. We will get back to you."

if __name__ == "__main__":
    print("🚀 Starting Chatbot App with SQLite...")
    app.run(debug=True, port=5001)
