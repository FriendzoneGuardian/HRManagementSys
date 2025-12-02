from flask import Blueprint, render_template
from app.models import Candidate, Department
from app import db

bp = Blueprint('main', __name__)

@bp.route('/')
@bp.route('/dashboard')
def dashboard():
    candidate_count = Candidate.query.count()
    department_count = Department.query.count()
    recent_candidates = Candidate.query.order_by(Candidate.application_date.desc()).limit(5).all()
    
    # Calculate average expected salary
    candidates = Candidate.query.all()
    total_salary = sum([c.expected_salary for c in candidates])
    avg_salary = total_salary / candidate_count if candidate_count > 0 else 0

    return render_template('dashboard.html', 
                           candidate_count=candidate_count, 
                           department_count=department_count,
                           recent_candidates=recent_candidates,
                           avg_salary=avg_salary)
