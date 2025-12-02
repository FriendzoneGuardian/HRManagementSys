# Project Horus

**Independent Academic Development Project**

## Overview

Project Horus is a modernized Recruitment Management System (RMS) designed to demonstrate an academically grounded yet forward‑oriented system architecture. Unlike production-grade corporate HR suites, Project Horus focuses on the hiring lifecycle, modularity, clarity, and demonstrability — allowing instructors to easily evaluate the system’s structure, logic, and technical implementation.

This project is fully **independent** and not part of SwiftSynapse Labs or SwiftGrade.

---

## 🚀 Current Development Phase

We are currently in the **Development Phase** under the Waterfall Model. Planning and design have been finalized, and the system is now transitioning into implementation based on approved specifications.

---

## 🏗️ Tech Stack

### **Backend**

* **Primary:** Flask (Python)
* **Database:** MySQL (via XAMPP)

### **Frontend**

* **Styling:** Tailwind CSS

---

## 🎯 Core Features

1.  **Dashboard Overview**: Key metrics and recent applications.
2.  **Candidate Management**: Track applicants and their status.
3.  **Job Applications**: (Coming Soon)
4.  **Interview Scheduling**: (Coming Soon)

---

## 📁 Project Structure

```
project-horus/
│
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── routes.py
│   ├── config.py
│   ├── run.py
│   └── populate_db.py
│
├── frontend/
│   ├── src/
│   │   └── input.css
│   ├── templates/
│   ├── static/
│   ├── package.json
│   └── tailwind.config.js
│
└── README.md
```

---

## 🔧 Installation & Setup

### 1. Clone Repository

```
git clone https://github.com/FriendzoneGuardian/HRManagementSys.git
cd HRManagementSys
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
cd frontend
npm install
npx tailwindcss -i ./src/input.css -o ./static/css/output.css --watch
```

### 5. Run Flask

```
python backend/run.py
```

---

## 📌 Project Direction

Project Horus aims to:

* Provide an academically demonstrable Recruitment System.
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
