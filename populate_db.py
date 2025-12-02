from app import create_app, db
from app.models import Employee, Department
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
            # Parse connection details (simplified for this specific case)
            # Assumes format: mysql+pymysql://user:pass@host:port/dbname
            from sqlalchemy.engine.url import make_url
            url = make_url(db_url)
            db_name = url.database
            
            # Connect without database selected
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
        # Create tables
        db.create_all()

        # Check if data already exists
        if Department.query.first():
            print("Database already populated.")
            return

        # Create Departments
        departments = ['HR', 'Engineering', 'Sales', 'Marketing', 'Finance']
        dept_objects = []
        for dept_name in departments:
            dept = Department(name=dept_name)
            db.session.add(dept)
            dept_objects.append(dept)
        
        db.session.commit()

        # Create Employees
        positions = ['Manager', 'Developer', 'Analyst', 'Specialist', 'Director']
        first_names = ['John', 'Jane', 'Alice', 'Bob', 'Charlie', 'Diana', 'Evan', 'Fiona']
        last_names = ['Doe', 'Smith', 'Johnson', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore']

        for i in range(20):
            dept = random.choice(dept_objects)
            emp = Employee(
                first_name=random.choice(first_names),
                last_name=random.choice(last_names),
                email=f'employee{i}@example.com',
                position=random.choice(positions),
                salary=random.randint(50000, 150000),
                department=dept,
                hire_date=datetime.now()
            )
            db.session.add(emp)
        
        db.session.commit()
        print("Database populated successfully!")

if __name__ == '__main__':
    populate()
