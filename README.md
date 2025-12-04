# 🦅 **Clarion HR Management System**

*(Formerly Project Horus)*

**Independent Academic Development Project**

## Overview

**Clarion** is a modern **HR Management System (HRMS)** developed under **Project Horus**, designed to streamline employee management, attendance tracking, and payroll processes through a clean, data-driven interface.
Inspired by *Horus*, the Egyptian god of foresight and protection, Clarion acts as the *watchful eye* over organizational operations — ensuring clarity, accountability, and performance transparency.

Unlike production-grade corporate HR suites, Clarion focuses on the hiring lifecycle, modularity, clarity, and demonstrability — allowing instructors to easily evaluate the system’s structure, logic, and technical implementation.

---

## 🚀 Current Development Phase

> [!IMPORTANT]
> **Core Functionalities Complete** (Phase 8.6)
> The system is now fully operational as a Recruitment & HR Management System.

We have successfully implemented:
*   **Job Management**: Posting, Editing, and Deleting Jobs.
*   **Applicant Lifecycle**: Registration, Application, Status Tracking, and Document Upload.
*   **HR Administration**: Candidate Management, Filtering, and Approval Workflows.
*   **Role-Based Access**: Distinct portals for Admin, HR, and Applicants.

---

## 🔮 Future Roadmap (TBD)

While the core system is complete, the following features are planned for future "DLC" updates:
*   **Email Notifications**: Automated emails for status changes.
*   **Interview Scheduling**: Calendar integration for setting up interviews.
*   **Analytics Dashboard**: Visual charts for hiring metrics.
*   **Profile Picture Upload**: Allow users to upload avatars.

---

## 🤖 AI Disclaimer

> [!NOTE]
> **Vibe Coded**
> This project was **100% AI-Generated** using advanced agentic coding workflows.
> Every line of code, documentation, and design decision was crafted by an AI Assistant (Antigravity) in collaboration with the user.
> *No humans were harmed (or coded) in the making of this software.*

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

### 4. Run the Application (Auto-Setup)

You can simply double-click **`run_setup.bat`** (Windows) or run:

```bash
python backend/run.py
```

**What happens next?**
1.  The system will automatically connect to your local MySQL server (default XAMPP settings).
2.  It will create the database `hr_management_sys` if it doesn't exist.
3.  It will create all necessary tables.
4.  It will create default accounts:
    *   **Admin**: `admin` / `admin123`
    *   **HR**: `hr` / `hr123`
5.  The server will start at `http://127.0.0.1:5000`.

### 5. Fresh Install (First Time Setup)

If you are running this on a newly installed PC, ensure you have the following prerequisites:
1.  **Python 3.10+**: [Download Here](https://www.python.org/downloads/) (Check "Add Python to PATH" during installation).
2.  **XAMPP (or MySQL Server)**: [Download Here](https://www.apachefriends.org/index.html) (Start Apache and MySQL modules).
3.  **Git**: [Download Here](https://git-scm.com/downloads).

Once installed, follow the standard installation steps above.

---

## ⚠️ Known Limitations

> [!WARNING]
> **Desktop Optimized**
> This application is currently optimized for **Desktop (1920x1080)** resolutions.
> Mobile and Tablet functionality is **experimental** and may experience layout issues. Please use a PC for the best experience.

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
