from flask import Blueprint, render_template
from app.models import Employee, Department
from app import db

bp = Blueprint('main', __name__)

@bp.route('/')
@bp.route('/dashboard')
def dashboard():
    employee_count = Employee.query.count()
    department_count = Department.query.count()
    recent_employees = Employee.query.order_by(Employee.hire_date.desc()).limit(5).all()
    
    # Calculate average salary
    employees = Employee.query.all()
    total_salary = sum([e.salary for e in employees])
    avg_salary = total_salary / employee_count if employee_count > 0 else 0

    return render_template('dashboard.html', 
                           employee_count=employee_count, 
                           department_count=department_count,
                           recent_employees=recent_employees,
                           avg_salary=avg_salary)
