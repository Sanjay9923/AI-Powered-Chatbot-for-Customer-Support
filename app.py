from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

# Ensure database file path is correct
DB_PATH = os.path.join(os.path.dirname(__file__), "chatbot.db")

# Connect to SQLite database. check_same_thread=False is needed for Flask threads.
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
cursor = conn.cursor()

# --- Database Setup (Ensuring both tables exist) ---
# Create FAQ table
cursor.execute("""
CREATE TABLE IF NOT EXISTS faq (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL
)
""")
# Create CONVERSATIONS table for logging
cursor.execute("""
CREATE TABLE IF NOT EXISTS conversations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_message TEXT,
    bot_reply TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()
# ----------------------------------------------------

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_text = request.form["msg"]
    bot_response = ""
    
    # Clean and standardize user input for better matching
    user_input_normalized = user_text.strip().lower()

    # Search for a matching question using the LIKE operator
    cursor.execute("SELECT answer FROM faq WHERE question LIKE ?", ('%' + user_input_normalized + '%',))
    result = cursor.fetchone()

    if result:
        # If a match is found, use the stored answer
        bot_response = result[0]
    else:
        # Fallback response if no match is found
        bot_response = "Sorry, I don't understand. We will get back to you."

    # --- LOGGING CONVERSATION ---
    try:
        cursor.execute(
            "INSERT INTO conversations (user_message, bot_reply) VALUES (?, ?)",
            (user_text, bot_response)
        )
        conn.commit()
    except Exception as e:
        print(f"Error logging conversation: {e}")
    # -----------------------------

    return bot_response

if __name__ == "__main__":
    print(" Starting Chatbot App with SQLite...")
    app.run(debug=True, port=5001)
