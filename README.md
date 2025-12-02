# Project Horus

**Independent Academic Development Project**

## Overview

Project Horus is a modernized Human Resource Management System (HRMS) designed to demonstrate an academically grounded yet forward‑oriented system architecture. Unlike production-grade corporate HR suites, Project Horus focuses on modularity, clarity, and demonstrability — allowing instructors to easily evaluate the system’s structure, logic, and technical implementation.

This project is fully **independent** and not part of SwiftSynapse Labs or SwiftGrade.

---

## 🚀 Current Development Phase

We are currently in the **Development Phase** under the Waterfall Model. Planning and design have been finalized, and the system is now transitioning into implementation based on approved specifications.

---

## 🏗️ Tech Stack

### **Backend Options (Final + Failover)**

* **Primary:** Flask (Python)
* **Styling:** Tailwind CSS
* **Emergency/Plan B:** Django (Python)

### **Database**

* **PostgreSQL** (Primary recommended — performance + reliability)

---

## 🎯 Core Features

1. Employee Records Management
2. Leave Management Workflow
3. Attendance Tracking Module
4. Role-Based Access Controls (RBAC)
5. Department & Position Structuring
6. HR Activity Logging
7. Dashboard Overview for Admin
8. Integrated Search & Filters
9. Modular API Endpoints
10. Clean UI powered by Tailwind

---

## 📁 Project Structure (Tentative)

```
project-horus/
│
├── backend/
│   ├── app.py (Flask main entry)
│   ├── routes/
│   ├── models/
│   └── services/
│
├── frontend/
│   ├── tailwind.config.js
│   ├── templates/
│   └── static/
│
├── database/
│   └── migrations/
│
└── README.md
```

---

## 🔧 Installation & Setup

### 1. Clone Repository

```
git clone https://github.com/your-username/project-horus.git
cd project-horus
```

### 2. Create Virtual Environment

```
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Initialize Tailwind

```
npm install
npx tailwindcss -i ./input.css -o ./static/css/output.css --watch
```

### 5. Run Flask

```
python app.py
```

---

## 📌 Project Direction

Project Horus aims to:

* Provide an academically demonstrable HRMS.
* Show proper design, modularity, and documentation.
* Maintain clarity and evaluability for instructors.
* Incorporate modern design conventions.

Django remains on standby as a fallback framework if needed.

---

## 📝 Notes

* This project is **independent** from SwiftSynapse Labs.
* Builds upon academic requirements rather than enterprise production constraints.
* All architectural decisions and changes are reflected across development logs.

---

## 📜 License

For academic purposes only.
