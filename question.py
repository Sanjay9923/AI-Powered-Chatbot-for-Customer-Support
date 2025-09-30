import sqlite3

conn = sqlite3.connect("chatbot.db")
cursor = conn.cursor()

faq_data = [
    ("hello", "Hi there! How can I assist you today?"),
    ("what is your name", "I am your AI-powered chatbot."),
    ("how are you", "I’m doing great, thanks for asking! How can I help you?"),
    ("what services do you provide", "I can assist with customer support, FAQs, and general queries."),
    ("how to contact support", "You can contact support via email at support@example.com."),
    ("what are your working hours", "We are available 24/7 to assist you."),
    ("where are you located", "Our headquarters is in Chennai, India."),
    ("how do I reset my password", "Click on 'Forgot Password' at login and follow the instructions."),
    ("do you store my data", "Yes, but only to improve our services and securely as per our privacy policy."),
    ("thank you", "You're welcome! Happy to help anytime.")
]

cursor.executemany("INSERT INTO faq (question, answer) VALUES (?, ?)", faq_data)
conn.commit()
conn.close()

print("✅ 10 FAQ entries inserted into chatbot.db")
