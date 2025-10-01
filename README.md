🌱 SanjeevaniAI

Conversations that Heal

SanjeevaniAI is an AI-powered mental health support system built for students.
It provides an empathetic chatbot, mood tracking, and secure counseling appointment scheduling.
Admins (counselors) can monitor alerts and bookings via a simple dashboard.

✨ Features

🤖 AI Chatbot – Detects risk level (low/medium/high) using ML model.

📊 Mood Tracking – Students log daily moods for self-reflection.

📅 Booking System – Collects student details (name, roll no, email, phone, address) and notifies counselor via email.

🚨 Alerts – High-risk messages are flagged and shown to admins in real time.

🔒 Private Journals – Journaling is student-only (not visible to admins).

🗄️ MongoDB Storage – All chats, moods, alerts, and bookings stored securely.

🛠️ Tech Stack

Backend: Python, Flask

Database: MongoDB

ML Model: Scikit-Learn (joblib model for risk detection)

Frontend: Flask templates (with option to integrate React/other frontend)

Notifications: SMTP (Gmail) for email alerts

🚀 Getting Started
1️⃣ Clone the repository
git clone https://github.com/Aditya-kr24/SanjeevaniAI.git
cd SanjeevaniAI

2️⃣ Set up a virtual environment (recommended)
python -m venv venv
# Activate venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Configure environment variables

Create a file named .env in the project root:

# MongoDB
MONGO_URI=mongodb://localhost:27017

# SMTP (Gmail example)
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=yourgmail@gmail.com
SMTP_PASS=your_app_password
COUNSELOR_EMAIL=counselor@example.com


⚠️ Use a Gmail App Password (not your regular Gmail password).

5️⃣ Run the Flask app
python app.py


The app will be available at 👉 http://127.0.0.1:5000/

📂 Project Structure
SanjeevaniAI/
│── app.py                 # Main Flask app
│── requirements.txt       # Python dependencies
│── utils/                 # Helper functions
│── templates/             # HTML templates
│── static/                # CSS / Images
│── model.joblib           # ML model (not in repo, add manually)
│── .env                   # Environment variables (not in repo)

👨‍💻 Admin Dashboard

/api/admin/alerts → Shows high-risk flagged messages

/api/admin/bookings → Shows booking requests (with “mark as done” + delete options)

(Students never see this — only admins with access should.)

🔮 Future Scope

Replace rule-based chatbot with Generative AI (LLM) for natural conversations.

Deploy on cloud (Render, Railway, AWS, Azure, etc.) with MongoDB Atlas.

Add SMS/WhatsApp notifications for urgent alerts.

Build dedicated React frontend for smoother UX.

🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to improve.

📜 License

This project is licensed under the MIT License.
