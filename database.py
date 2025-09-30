import sqlite3

# Connect to database (creates file if not exists)
conn = sqlite3.connect("chatbot.db", check_same_thread=False)
cursor = conn.cursor()

# Create a table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS conversations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_message TEXT,
    bot_reply TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
print("Database ready!")

# Insert a sample conversation
cursor.execute("INSERT INTO conversations (user_message, bot_reply) VALUES (?, ?)",
               ("Hello", "Hi, how can I help you?"))
conn.commit()

# Fetch data
cursor.execute("SELECT * FROM conversations")
print(cursor.fetchall())
