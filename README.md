# CALMCONNECT – AI & HUMAN-ASSISTED THERAPY CHAT
# Introduction
CalmConnect is a therapy chatbot web application designed to provide seamless interaction between users, AI-powered assistance, and real human therapists (agents).

Users can create a chat room to start a session.
Admins manage the platform by creating and verifying agents before they can engage with users.
Agents provide human-assisted therapy once verified by an admin.
The platform ensures secure, structured, and real-time conversations to enhance mental health support.
# Features
✅ User-Created Chat Rooms – Users create their own chat rooms for therapy sessions.

✅ Admin & Agent System – Admins verify agents before they can chat with users.

✅ Real-Time Communication – Chat functionality using HTML, JavaScript, and Django channels.

✅ Secure & Scalable – Built with Django for robust session handling.

✅ Minimalist UI – Clean and intuitive frontend with HTML, CSS (Tailwind), and JavaScript.

# Technology 
# Component	Technology Used

Backend:Django (Python)

Frontend:HTML, CSS (Tailwind), JavaScript.

Database: SQLite

Authentication: Django Auth

Real-Time Chat: Django Channels (WebSockets)

# Installation Guide
# 1. Clone the Repository
git clone https://github.com/rillhancho/calm-connect-realtime-chat
cd calm-connect-realtime-chat
# 2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
# 3. Install Dependencies
pip install -r requirements.txt
# 4. Run Migrations
python manage.py migrate
# 5. Create a Superuser (Admin)
python manage.py createsuperuser
# 6. Start the Django Development Server
python manage.py runserver
# 7. Access the Web App
Go to http://127.0.0.1:8000/ in your browser.
# How It Works
# 1. User Flow
User creates a chat room.
An available agent or admin joins the chat.
User can communicate with either the AI bot or a human agent.
If no agent is available, the AI provides initial support.
# 2. Admin Role
Admins can create and verify agents before they interact with users.
Only verified agents can join user chat rooms. Admin is the only one who can modify chatrooms.
# 3. Agent Role
Agents must be verified by an admin before accessing chat rooms.
Verified agents can join chat rooms and provide support.



