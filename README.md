# AI-Powered Chatbot for Customer Support
## Overview

This project is an AI-powered chatbot designed to help customers get quick answers to common questions. It uses natural language processing techniques to understand user queries and provide accurate, context-aware responses.
The system includes a simple web interface where users can ask questions, and the chatbot replies instantly based on the knowledge stored in the question files.


## Key Features

&bull; Real-time customer support chatbot

&bull; Understands user queries using simple NLP logic

&bull; Clean and responsive web interface

&bull; Easy to expand by adding new question–answer pairs

&bull; MySQL database support for storing chat data

&bull; Lightweight and easy to set up


## How It Works

1.**User Opens the Chatbot** – The user visits the main page (index.html) in their browser.

2.**User Sends a Question** – The user types a query in the chatbot interface.

3.**Backend Processing** – The Flask application (app.py) receives the query and passes it to the chatbot logic.

4.**Question Matching** – The chatbot checks the question files or dataset to find the most relevant answer.

5.**Response Generation** – The chatbot generates a context-aware response based on the matching logic or NLP model.

6.**Display Response** – The answer is sent back to the frontend and displayed in the chat window instantly.

7.**Optional Logging** – The conversation can be saved in the database for analysis or future improvements.


## Tech Stack

**Python** – Backend logic

**Flask** – Web framework

**HTML, CSS, JavaScript** – Frontend UI

**MySQL** – Database for chat storage

**AI / NLP** – Used for matching user questions

**Custom Question Files** – Extendable knowledge base


## Installation and Setup
1.**Clone the Repository**
git clone https://github.com/Sanjay9923/AI-Powered-Chatbot-for-Customer-Support.git
cd AI-Powered-Chatbot-for-Customer-Support

2.**Create a Virtual Environment**
python -m venv venv

Activate it:

venv\Scripts\activate

3.**Install Required Libraries**
pip install -r requirements.txt

4.**Set Up the Database**

Open MySQL or phpMyAdmin:

CREATE DATABASE chatbot_db;

Import the SQL file located in the database folder.

5.**Update Database Credentials (if required)**

Inside app.py, check your MySQL login settings:

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="chatbot_db"
)

6.**Run the Application**
python app.py

7.**Open the App**

Open your browser and go to:

http://127.0.0.1:5000/


## Project Structure
AI-Powered-Chatbot-for-Customer-Support/

│
├── app.py                 # Main Flask application  
│
├── templates/             # HTML pages  
│   ├── index.html         # Chatbot interface  
│   └── chatbot.html       # (If separate page)  
│
├── static/                # CSS, JS, images  
│   ├── css/  
│   ├── js/  
│   └── images/  
│
├── database/              # SQL database file  
│   └── chatbot_db.sql  
│
├── questions/             # Dataset used by the chatbot  
│   └── data.json / .txt  
│
└── requirements.txt       # Python dependencies  


## System Architecture

User → Web Interface (HTML/CSS/JS)
        │
        ▼
   Flask Backend (app.py)
        │
        ▼
  Chatbot Logic / NLP
        │
        ▼
  Question Files / Knowledge Base
        │
        ▼
     MySQL Database


## Future Improvements

Add more advanced NLP models for better accuracy

Add a full admin dashboard for FAQ and analytics

Add user login using Flask

Support for multiple languages

Integrate voice support or external chat platforms

## Project Contributor

**Sanjay.s** — Developer and Project Lead
Contributions are welcome. Feel free to submit pull requests or suggest improvements.

## License

This project is open-source and available under the MIT License.
