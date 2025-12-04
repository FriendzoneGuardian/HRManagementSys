"""
Clarion HRMS - Main Routes
==========================
Purpose:
    Handles core application logic for Admin and HR roles.
    Includes Dashboard, Candidate Management, Job Management, and Approvals.

Key Routes:
    - /dashboard: Main overview.
    - /candidates: CRUD for candidates.
    - /jobs: CRUD for job postings.
    - /approvals: Admin approval for new accounts.

Author: Antigravity AI
"""

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import Candidate, Department, AuditLog, User, JobPosting
from app import db
from sqlalchemy import func
from datetime import datetime

bp = Blueprint('main', __name__)

@bp.route('/')
@bp.route('/dashboard')
@login_required
def dashboard():
    if current_user.role == 'Applicant':
        return redirect(url_for('applicant.dashboard'))
        
    candidate_count = Candidate.query.count()
    department_count = Department.query.count()
    recent_candidates = Candidate.query.order_by(Candidate.application_date.desc()).limit(5).all()
    
    # Optimization: Calculate average salary in DB
    avg_salary = db.session.query(func.avg(Candidate.expected_salary)).scalar() or 0

    return render_template('dashboard.html', 
                           candidate_count=candidate_count, 
                           department_count=department_count,
                           recent_candidates=recent_candidates,
                           avg_salary=avg_salary)

from app.forms import CandidateForm, JobForm

from app.utils import log_user_action

@bp.route('/candidates', methods=['GET'])
@login_required
def candidates():
    search_query = request.args.get('search', '')
    department_filter = request.args.get('department', '')
    status_filter = request.args.get('status', '')

    query = Candidate.query

    if search_query:
        query = query.filter(
            (Candidate.first_name.ilike(f'%{search_query}%')) |
            (Candidate.last_name.ilike(f'%{search_query}%')) |
            (Candidate.email.ilike(f'%{search_query}%')) |
            (Candidate.position.ilike(f'%{search_query}%'))
        )
    
    if department_filter:
        query = query.filter(Candidate.department_id == department_filter)
    
    if status_filter:
        query = query.filter(Candidate.status == status_filter)

    candidates = query.order_by(Candidate.application_date.desc()).all()
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

@bp.route('/admin/approvals', methods=['GET', 'POST'])
@login_required
def approvals():
    if current_user.role != 'Admin':
        flash('Permission denied.', 'error')
        return redirect(url_for('main.dashboard'))
        
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        action = request.form.get('action')
        user = User.query.get(user_id)
        
        if user:
            if action == 'approve':
                user.is_approved = True
                flash(f'User {user.username} approved.', 'success')
                log_user_action('APPROVE_USER', f"Approved user {user.username}")
            elif action == 'reject':
                db.session.delete(user)
                flash(f'User {user.username} rejected and deleted.', 'warning')
                log_user_action('REJECT_USER', f"Rejected user {user.username}")
            db.session.commit()
            
    pending_users = User.query.filter_by(is_approved=False).all()
    return render_template('approvals.html', users=pending_users)

@bp.route('/jobs', methods=['GET'])
@login_required
def jobs():
    if current_user.role not in ['Admin', 'HR']:
        flash('Permission denied.', 'error')
        return redirect(url_for('main.dashboard'))
        
    jobs = JobPosting.query.order_by(JobPosting.posted_date.desc()).all()
    departments = Department.query.all()
    form = JobForm()
    return render_template('jobs.html', jobs=jobs, departments=departments, form=form)

@bp.route('/jobs/add', methods=['POST'])
@login_required
def add_job():
    if current_user.role not in ['Admin', 'HR']:
        flash('Permission denied.', 'error')
        return redirect(url_for('main.dashboard'))
        
    form = JobForm()
    if form.validate_on_submit():
        try:
            department = Department.query.get(form.department.data)
            new_job = JobPosting(
                title=form.title.data,
                department=department,
                requirements=form.requirements.data,
                status=form.status.data,
                posted_date=datetime.now()
            )
            db.session.add(new_job)
            db.session.commit()
            log_user_action('ADD_JOB', f"Posted job {new_job.title}")
            flash('Job posted successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error posting job: {str(e)}', 'error')
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f"Error in {getattr(form, field).label.text}: {error}", 'error')
                
    return redirect(url_for('main.jobs'))

@bp.route('/jobs/<int:id>/edit', methods=['POST'])
@login_required
def edit_job(id):
    if current_user.role not in ['Admin', 'HR']:
        flash('Permission denied.', 'error')
        return redirect(url_for('main.dashboard'))
        
    job = JobPosting.query.get_or_404(id)
    form = JobForm()
    
    if form.validate_on_submit():
        try:
            job.title = form.title.data
            job.department = Department.query.get(form.department.data)
            job.requirements = form.requirements.data
            job.status = form.status.data
            
            db.session.commit()
            log_user_action('EDIT_JOB', f"Edited job {job.title}")
            flash('Job updated successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating job: {str(e)}', 'error')
            
    return redirect(url_for('main.jobs'))

@bp.route('/jobs/<int:id>/delete', methods=['POST'])
@login_required
def delete_job(id):
    if current_user.role not in ['Admin', 'HR']:
        flash('Permission denied.', 'error')
        return redirect(url_for('main.dashboard'))
        
    job = JobPosting.query.get_or_404(id)
    try:
        title = job.title
        db.session.delete(job)
        db.session.commit()
        log_user_action('DELETE_JOB', f"Deleted job {title}")
        flash('Job deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting job: {str(e)}', 'error')
        
    return redirect(url_for('main.jobs'))
