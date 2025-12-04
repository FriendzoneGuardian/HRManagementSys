"""
Clarion HRMS - Setup Script
===========================
Purpose:
    Initializes the database, creates schema, and seeds default data.
    Acts as the "Installer" for the application.

Actions:
    1. Connects to MySQL (XAMPP default).
    2. Creates database 'hr_management_sys' if missing.
    3. Creates all tables.
    4. Seeds Departments (IT, Finance, HR, Sales).
    5. Seeds Default Users (Admin, HR).
    6. Seeds Sample Jobs.

Usage:
    python backend/setup.py

Author: Antigravity AI
"""

import os
import sys
import pymysql
from sqlalchemy import text
from sqlalchemy.engine.url import make_url

# Add the current directory to sys.path to ensure imports work
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import create_app, db
from app.models import User, Department
from config import Config

def setup_database():
    print("--- 🦅 Clarion HRMS Setup 🦅 ---")
    
    # 1. Database Creation (Literal Database Creation)
    db_url = Config.SQLALCHEMY_DATABASE_URI
    if 'mysql' in db_url:
        try:
            url = make_url(db_url)
            db_name = url.database
            
            # Connect to MySQL Server (defaulting to XAMPP settings if needed)
            # We connect without selecting a database first
            print(f"[*] Connecting to MySQL Server at {url.host}...")
            conn = pymysql.connect(
                host=url.host,
                user=url.username,
                password=url.password or '',
                port=url.port or 3306
            )
            cursor = conn.cursor()
            
            # Check/Create Database
            print(f"[*] Checking database '{db_name}'...")
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
            conn.commit()
            conn.close()
            print(f"[+] Database '{db_name}' ready.")
            
        except Exception as e:
            print(f"[-] Error checking/creating database: {e}")
            print("    Please ensure XAMPP (MySQL) is running.")
            return False

    # 2. Schema Initialization & Seeding
    app = create_app()
    with app.app_context():
        try:
            print("[*] Initializing schema...")
            db.create_all()
            
            # 3. Default Departments (Hybrid IT-Accounting Template)
            departments = ['IT Solutions', 'Accounting & Finance', 'HR & Admin', 'Sales & Growth']
            dept_objects = {}
            for dept_name in departments:
                dept = Department.query.filter_by(name=dept_name).first()
                if not dept:
                    dept = Department(name=dept_name)
                    db.session.add(dept)
                    print(f"    + Created Department: {dept_name}")
                dept_objects[dept_name] = dept
            
            db.session.commit() # Commit to get IDs

            # 4. Sample Jobs (Template Data)
            # We need to re-fetch departments to ensure they are attached to the session
            from app.models import JobPosting
            
            sample_jobs = [
                ('Senior Full Stack Developer', 'IT Solutions', '5+ years Python, React, AWS. Leadership experience required.'),
                ('System Administrator', 'IT Solutions', 'Linux, Windows Server, Azure, Networking.'),
                ('IT Support Specialist', 'IT Solutions', 'Helpdesk support, hardware troubleshooting, customer service.'),
                ('Forensic Accountant', 'Accounting & Finance', 'CPA, Fraud detection, Audit experience.'),
                ('Payroll Specialist', 'Accounting & Finance', 'ADP, Payroll processing, Tax compliance.'),
                ('Tax Consultant', 'Accounting & Finance', 'Corporate tax planning, IRS regulations.'),
                ('HR Manager', 'HR & Admin', 'Employee relations, Policy development, Recruitment strategy.'),
                ('Recruitment Specialist', 'HR & Admin', 'Sourcing, Interviewing, ATS management.'),
                ('Enterprise Sales Rep', 'Sales & Growth', 'B2B sales, CRM experience, Negotiation skills.'),
                ('Growth Marketer', 'Sales & Growth', 'SEO, SEM, Content Marketing, Analytics.')
            ]

            for title, dept_name, reqs in sample_jobs:
                dept = Department.query.filter_by(name=dept_name).first()
                if dept and not JobPosting.query.filter_by(title=title).first():
                    job = JobPosting(title=title, department=dept, requirements=reqs, status='Open')
                    db.session.add(job)
                    print(f"    + Created Job: {title}")

            # 5. Default Users (Admin & HR)
            # Admin
            if not User.query.filter_by(username='admin').first():
                admin = User(username='admin', role='Admin', is_approved=True)
                admin.set_password('admin123')
                db.session.add(admin)
                print("    + Created Admin Account (admin/admin123)")
            
            # HR
            if not User.query.filter_by(username='hr').first():
                hr = User(username='hr', role='HR', is_approved=True)
                hr.set_password('hr123')
                db.session.add(hr)
                print("    + Created HR Account (hr/hr123)")

            db.session.commit()
            print("[+] Setup Complete! System is ready.")
            return True
            
        except Exception as e:
            print(f"[-] Error during schema/seeding: {e}")
            return False

if __name__ == '__main__':
    setup_database()
