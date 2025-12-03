from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import Candidate, Department
from app import db

bp = Blueprint('main', __name__)

@bp.route('/')
@bp.route('/dashboard')
@login_required
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

@bp.route('/candidates')
@login_required
def candidates():
    candidates = Candidate.query.order_by(Candidate.application_date.desc()).all()
    departments = Department.query.all()
    return render_template('candidates.html', candidates=candidates, departments=departments)

@bp.route('/candidates/add', methods=['POST'])
@login_required
def add_candidate():
    try:
        department_id = request.form.get('department')
        department = Department.query.get(department_id)
        
        new_candidate = Candidate(
            first_name=request.form.get('first_name'),
            last_name=request.form.get('last_name'),
            email=request.form.get('email'),
            position=request.form.get('position'),
            department=department,
            expected_salary=float(request.form.get('expected_salary')),
            status=request.form.get('status'),
            application_date=datetime.now()
        )
        
        db.session.add(new_candidate)
        db.session.commit()
        flash('Candidate added successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error adding candidate: {str(e)}', 'error')
        
    return redirect(url_for('main.candidates'))

@bp.route('/candidates/<int:id>/edit', methods=['POST'])
@login_required
def edit_candidate(id):
    candidate = Candidate.query.get_or_404(id)
    try:
        candidate.first_name = request.form.get('first_name')
        candidate.last_name = request.form.get('last_name')
        candidate.email = request.form.get('email')
        candidate.position = request.form.get('position')
        candidate.expected_salary = float(request.form.get('expected_salary'))
        candidate.status = request.form.get('status')
        
        department_id = request.form.get('department')
        if department_id:
            candidate.department = Department.query.get(department_id)
            
        db.session.commit()
        flash('Candidate updated successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error updating candidate: {str(e)}', 'error')
        
    return redirect(url_for('main.candidates'))

@bp.route('/candidates/<int:id>/delete', methods=['POST'])
@login_required
def delete_candidate(id):
    if current_user.role != 'Admin':
        flash('Permission denied: Only Admins can delete candidates.', 'error')
        return redirect(url_for('main.candidates'))

    candidate = Candidate.query.get_or_404(id)
    try:
        db.session.delete(candidate)
        db.session.commit()
        flash('Candidate deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting candidate: {str(e)}', 'error')
        
    return redirect(url_for('main.candidates'))
