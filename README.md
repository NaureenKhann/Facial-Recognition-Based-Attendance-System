🎓 Face Recognition-Based Attendance System
📌 Project Overview
This project is a Face Recognition-Based Attendance System designed to automate and secure the process of tracking student attendance using advanced facial recognition technology. Built with Python, OpenCV, MySQL, and Tkinter, the system ensures high accuracy, real-time performance, and a user-friendly interface.A Facial Recognition-Based Attendance System is an automated solution that uses facial recognition technology to identify individuals and mark their attendance. The system captures live images or video, processes them to detect and match faces against a pre-stored database, and records attendance accurately. It saves time consumption

💡 “Say goodbye to proxies and manual registers – this system ensures verified and streamlined attendance in academic environments.”

✨ Key Features
✅ Face Recognition
Real-time face detection and recognition using Haar Cascade and LBPH algorithm.

Collects 50 grayscale image samples per student during training.

High accuracy even under varying lighting conditions.

✅ Automated Attendance
Attendance marked automatically upon successful face recognition.

Status stored as “Present” in a MySQL database along with timestamp and date.

CSV export of attendance records for backup or reporting.

✅ Absentee Notification (📲 Twilio Integration)
WhatsApp messages sent automatically at 12 PM daily to parents of absent students.

Ensures parental involvement and discipline in the classroom.

✅ Text-to-Speech (TTS)
When attendance is marked, a voice output confirms: “Attendance Marked”.

Interactive and accessible environment using the pyttsx3 library.

✅ Graphical User Interface (Tkinter)
Simple and intuitive GUI with the following modules:

Student Details: Add, update, delete student records.

Train Data: Capture face samples and train recognition model.

Face Recognition: Live detection to mark attendance.

Attendance: View, update, export attendance data.

Help Desk: AI chatbot to answer user queries.

Photos: View all saved face samples.

About Us: Developer info with a TTS description.

Exit: Exit the system securely.

🛠 Technology Stack
Component	Technology
Programming	Python
GUI Framework	Tkinter
Database	MySQL
Face Recognition	OpenCV (HaarCascade + LBPH)
Voice Feedback	pyttsx3
API Integration	Twilio WhatsApp API
Image Handling	PIL (Pillow)

📸 System Interface Overview
Student Form: Register students with department, semester, contact details.

Attendance Panel: Automatically logs date/time/department.

AI Chatbot: Provides help and answers FAQs.

Real-Time Panel: Live camera feed to detect and match faces.

Training UI: Visual feedback while training samples.

Developer Page: Details about contributors with TTS project description.

📦 Folder Structure
bash
Copy
Edit
Attendance-System/
│
├── data/                   # Saved face samples
├── attendance/             # CSV logs
├── trainer/                # Trained LBPH model
├── photos/                 # Captured student images
├── main.py                 # Entry point
├── student.py              # Student registration
├── train.py                # Training logic
├── face_recognition.py     # Recognition logic
├── attendance.py           # Attendance view/export
├── chatbot.py              # Help desk chatbot
├── developer.py            # Developer info GUI
├── db_config.py            # MySQL connection settings
├── utils.py                # Helper functions
└── README.md               # This file
👥 Contributors
Naureen Khan – Lead Developer [23AI04]

Shaikh Mariya Shakeel Ahmed – UI/UX Designer [23AI12]

Insha Khan – Database Specialist [23AI03]

Muskan Mustaqeem Kurawle – Testing Engineer [24DAI07]

Proudly developed by Team Hack Her Way from AIML Department (2nd Year).

🚀 Future Enhancements
📱 Mobile App Integration (Android/iOS)

📊 Live Analytics Dashboard

😊 Emotion Detection for Engagement

🔐 Multi-Factor Authentication (MFA) for enhanced security

🌐 Cloud Storage Integration for scalable data management
