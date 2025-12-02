from app import create_app, db
from app.models import Candidate, Department
from datetime import datetime
import random

app = create_app()

def populate():
    import pymysql
    from config import Config
    
    # Create database if it doesn't exist
    db_url = Config.SQLALCHEMY_DATABASE_URI
    if 'mysql' in db_url:
        try:
            from sqlalchemy.engine.url import make_url
            url = make_url(db_url)
            db_name = url.database
            
            conn = pymysql.connect(
                host=url.host,
                user=url.username,
                password=url.password or '',
                port=url.port or 3306
            )
            cursor = conn.cursor()
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
            conn.close()
            print(f"Database '{db_name}' checked/created.")
        except Exception as e:
            print(f"Error creating database: {e}")

    with app.app_context():
        # Drop legacy 'employee' table if it exists (to fix FK constraints)
        try:
            db.session.execute(db.text("DROP TABLE IF EXISTS employee"))
            db.session.commit()
            print("Dropped legacy 'employee' table.")
        except Exception as e:
            print(f"Warning: Could not drop 'employee' table: {e}")

        # Drop all tables to reset schema
        db.drop_all()
        db.create_all()

        # Create Departments
        departments = ['HR', 'Engineering', 'Sales', 'Marketing', 'Finance']
        dept_objects = []
        for dept_name in departments:
            dept = Department(name=dept_name)
            db.session.add(dept)
            dept_objects.append(dept)
        
        db.session.commit()

        # Create Candidates
        positions = ['Manager', 'Developer', 'Analyst', 'Specialist', 'Director']
        first_names = ['John', 'Jane', 'Alice', 'Bob', 'Charlie', 'Diana', 'Evan', 'Fiona']
        last_names = ['Doe', 'Smith', 'Johnson', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore']
        statuses = ['Applied', 'Interviewing', 'Offer', 'Rejected']

        for i in range(20):
            dept = random.choice(dept_objects)
            cand = Candidate(
                first_name=random.choice(first_names),
                last_name=random.choice(last_names),
                email=f'candidate{i}@example.com',
                position=random.choice(positions),
                expected_salary=random.randint(50000, 150000),
                department=dept,
                application_date=datetime.now(),
                status=random.choice(statuses)
            )
            db.session.add(cand)
        
        db.session.commit()
        print("Database populated with Candidates successfully!")

if __name__ == '__main__':
    populate()
