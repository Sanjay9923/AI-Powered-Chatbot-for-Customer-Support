# AI-Powered Chatbot for Customer Support

## Overview

This project is an AI-powered chatbot designed to help customers get quick answers to common questions. It uses natural language processing techniques to understand user queries and provide accurate, context-aware responses.
The system includes a simple web interface where users can ask questions, and the chatbot replies instantly based on the knowledge stored in the question files.


## Preview (Screenshot) 
![Screenshot (42) (1)](https://github.com/user-attachments/assets/12fbc705-52f0-4003-b8b8-24bd13fe3a78)



## Features

- Real-time customer support chatbot

- Understands user queries using simple NLP logic

- Clean and responsive web interface

- Easy to expand by adding new question–answer pairs

- MySQL database support for storing chat data

- Lightweight and easy to set up


## How It Works

1.**User Opens the Chatbot** – The user visits the main page (index.html) in their browser.

2.**User Sends a Question** – The user types a query in the chatbot interface.

3.**Backend Processing** – The Flask application (app.py) receives the query and passes it to the chatbot logic.

4.**Question Matching** – The chatbot checks the question files or dataset to find the most relevant answer.

5.**Response Generation** – The chatbot generates a context-aware response based on the matching logic or NLP model.

6.**Display Response** – The answer is sent back to the frontend and displayed in the chat window instantly.

7.**Optional Logging** – The conversation can be saved in the database for analysis or future improvements.


## Project Structure

```bash
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
 └── data.json / .txt  
```


## Technologies Used

**Python** – Backend logic

**Flask** – Web framework

**HTML, CSS, JavaScript** – Frontend UI

**MySQL** – Database for chat storage

**AI / NLP** – Used for matching user questions

**Custom Question Files** – Extendable knowledge base


## Getting Started

Follow these steps to run the AI-Powered Chatbot for Customer Support on your local machine.

1.**Clone or Download the Project**
```bash
git clone https://github.com/Sanjay9923/AI-Powered-Chatbot-for-Customer-Support.git
```

Move into the project folder:
```bash
cd "AI-Powered Chatbot for Customer Support"
```

2.**Install Required Dependencies**

This project uses Flask. Install it with:
```bash
pip install flask
```
No other external libraries are required because SQLite is built into Python.

3.**Start the Chatbot Server**

Run the Flask application:
```bash
python app.py
```
If everything loads correctly, you will see something like:
```nginx
Running on http://127.0.0.1:5001
```

4.**Open the Chatbot in Your Browser**

Go to:
```ccp
http://127.0.0.1:5001
```
The chatbot interface will appear, and you can start asking questions immediately.

5.**Using the Chatbot**

Type your query into the text box.

The system checks your question against saved FAQ entries in chatbot.db.

It returns the most relevant answer or a fallback message if no match is found.


## Future Improvements

- Add more advanced NLP models for better accuracy

- Add a full admin dashboard for FAQ and analytics

- Add user login using Flask

- Support for multiple languages

- Integrate voice support or external chat platforms


## Project Contributor

Sanjay.s — Developer and Project Lead

Contributions are welcome. Feel free to submit pull requests or suggest improvements.


## License

This project is **free to use** and does not contains any license.



