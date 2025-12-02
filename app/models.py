from app import db
from datetime import datetime

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    employees = db.relationship('Employee', backref='department', lazy='dynamic')

    def __repr__(self):
        return f'<Department {self.name}>'

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True)
    last_name = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    position = db.Column(db.String(64))
    hire_date = db.Column(db.DateTime, default=datetime.utcnow)
    salary = db.Column(db.Float)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    
    def __repr__(self):
        return f'<Employee {self.first_name} {self.last_name}>'
