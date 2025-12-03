# 🦅 **Clarion HR Management System**

*(Formerly Project Horus)*

**Independent Academic Development Project**

## Overview

**Clarion** is a modern **HR Management System (HRMS)** developed under **Project Horus**, designed to streamline employee management, attendance tracking, and payroll processes through a clean, data-driven interface.
Inspired by *Horus*, the Egyptian god of foresight and protection, Clarion acts as the *watchful eye* over organizational operations — ensuring clarity, accountability, and performance transparency.

Unlike production-grade corporate HR suites, Clarion focuses on the hiring lifecycle, modularity, clarity, and demonstrability — allowing instructors to easily evaluate the system’s structure, logic, and technical implementation.

---

## 🚀 Current Development Phase

We have completed **Phase 6** (Applicant Module & System Hardening). The system now includes a full Applicant lifecycle, from registration and document upload to admin approval and status tracking.

---

## 🏗️ Tech Stack

### **Backend**

* **Primary:** Python (Flask Framework)
* **Database:** SQLite (Dev) / MySQL (Production via XAMPP)
* **ORM:** Flask-SQLAlchemy
* **Auth:** Flask-Login & Flask-WTF

### **Frontend**

* **Styling:** Tailwind CSS (Utility-first)
* **Templating:** Jinja2
* **Interactivity:** Vanilla JS / Flowbite Components

### **Project Structure**

```
HRManagementSys/
│
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── routes.py
│   │   ├── auth.py
│   │   ├── forms.py
│   │   └── utils.py
│   ├── config.py
│   ├── run.py
│   └── populate_db.py
│
├── frontend/
│   ├── src/
│   │   └── input.css
│   ├── templates/
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   ├── package.json
│   └── tailwind.config.js
│
└── README.md
```

---

## 🔧 Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/FriendzoneGuardian/HRManagementSys.git
cd HRManagementSys
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Initialize Tailwind

```bash
cd frontend
npm install
npm run build
```

### 5. Run Flask

```bash
# From the root directory
python backend/run.py
```

---

## 🌟 Unique Features — Clarion Edge

1.  **Data-Driven Insights** for attendance trends.
2.  **HR Pulse View** dashboard.
3.  **Modular API Integration**.
4.  **Minimalist Tailwind UI** with Role-Based Theming (Blue for Admin, Violet for HR).
5.  **Secure Authentication** with Flask-Login and CSRF protection.
6.  **Audit Logging** for accountability.
7.  **Applicant Module**: Dedicated dashboard for candidates to view jobs and track status.
8.  **Approval Workflow**: Admin verification for new account registrations.

---

## 📌 Project Direction

**Clarion** aims to:

*   Provide an academically demonstrable Recruitment System.
*   Show proper design, modularity, and documentation.
*   Maintain clarity and evaluability for instructors.
*   Incorporate modern design conventions.

---

## 📜 License

For academic purposes only.
