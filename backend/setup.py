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
            
            # 3. Default Departments
            departments = ['HR', 'Engineering', 'Sales', 'Marketing', 'Finance']
            for dept_name in departments:
                if not Department.query.filter_by(name=dept_name).first():
                    db.session.add(Department(name=dept_name))
                    print(f"    + Created Department: {dept_name}")
            
            # 4. Default Users (Admin & HR)
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
