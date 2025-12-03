from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import Candidate, Department, AuditLog
from app import db
from datetime import datetime

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

from app.forms import CandidateForm

from app.utils import log_user_action

@bp.route('/candidates', methods=['GET'])
@login_required
def candidates():
    candidates = Candidate.query.order_by(Candidate.application_date.desc()).all()
    departments = Department.query.all()
    form = CandidateForm()
    return render_template('candidates.html', candidates=candidates, departments=departments, form=form)

@bp.route('/candidates/add', methods=['POST'])
@login_required
def add_candidate():
    form = CandidateForm()
    if form.validate_on_submit():
        try:
            department = Department.query.get(form.department.data)
            
            new_candidate = Candidate(
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                email=form.email.data,
                position=form.position.data,
                department=department,
                expected_salary=form.expected_salary.data,
                status=form.status.data,
                application_date=datetime.now()
            )
            
            db.session.add(new_candidate)
            db.session.commit()
            log_user_action('ADD_CANDIDATE', f"Added candidate {new_candidate.first_name} {new_candidate.last_name}")
            flash('Candidate added successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding candidate: {str(e)}', 'error')
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Error in {getattr(form, field).label.text}: {error}", 'error')
        
    return redirect(url_for('main.candidates'))

@bp.route('/candidates/<int:id>/edit', methods=['POST'])
@login_required
def edit_candidate(id):
    candidate = Candidate.query.get_or_404(id)
    form = CandidateForm()
    
    if form.validate_on_submit():
        try:
            candidate.first_name = form.first_name.data
            candidate.last_name = form.last_name.data
            candidate.email = form.email.data
            candidate.position = form.position.data
            candidate.expected_salary = form.expected_salary.data
            candidate.status = form.status.data
            candidate.department = Department.query.get(form.department.data)
            
            db.session.commit()
            log_user_action('EDIT_CANDIDATE', f"Edited candidate {candidate.first_name} {candidate.last_name}")
            flash('Candidate updated successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating candidate: {str(e)}', 'error')
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Error in {getattr(form, field).label.text}: {error}", 'error')
        
    return redirect(url_for('main.candidates'))

@bp.route('/candidates/<int:id>/delete', methods=['POST'])
@login_required
def delete_candidate(id):
    if current_user.role != 'Admin':
        flash('Permission denied: Only Admins can delete candidates.', 'error')
        return redirect(url_for('main.candidates'))

    candidate = Candidate.query.get_or_404(id)
    try:
        name = f"{candidate.first_name} {candidate.last_name}"
        db.session.delete(candidate)
        db.session.commit()
        log_user_action('DELETE_CANDIDATE', f"Deleted candidate {name}")
        flash('Candidate deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting candidate: {str(e)}', 'error')
        
    return redirect(url_for('main.candidates'))

@bp.route('/audit-logs')
@login_required
def audit_logs():
    if current_user.role != 'Admin':
        flash('Permission denied: Only Admins can view audit logs.', 'error')
        return redirect(url_for('main.dashboard'))
        
    logs = AuditLog.query.order_by(AuditLog.timestamp.desc()).all()
    return render_template('audit_logs.html', logs=logs)
