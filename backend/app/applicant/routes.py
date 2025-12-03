from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.applicant import bp
from app.models import JobPosting, CandidateDocument, Candidate
from werkzeug.utils import secure_filename
import os
from datetime import datetime

@bp.route('/dashboard')
@login_required
def dashboard():
    if current_user.role != 'Applicant':
        return redirect(url_for('main.dashboard'))
    
    # Dummy data for job postings if none exist
    jobs = JobPosting.query.filter_by(status='Open').all()
    if not jobs:
        # Create dummy jobs if empty (for demo purposes)
        dummy_jobs = [
            JobPosting(title='Software Engineer', department_id=1, requirements='Python, Flask, SQL'),
            JobPosting(title='HR Specialist', department_id=1, requirements='Communication, Management'),
            JobPosting(title='Data Analyst', department_id=1, requirements='Excel, Python, Tableau')
        ]
        # We need department_id to be valid. Assuming departments exist.
        # If not, we skip creating dummy data here to avoid errors.
        pass

    return render_template('applicant/dashboard.html', title='My Dashboard', jobs=jobs)

@bp.route('/upload', methods=['POST'])
@login_required
def upload_document():
    if 'document' not in request.files:
        flash('No file part', 'error')
        return redirect(url_for('applicant.dashboard'))
    
    file = request.files['document']
    if file.filename == '':
        flash('No selected file', 'error')
        return redirect(url_for('applicant.dashboard'))
        
    if file:
        filename = secure_filename(file.filename)
        # Ensure uploads directory exists
        upload_folder = os.path.join(os.getcwd(), 'uploads')
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
            
        file.save(os.path.join(upload_folder, filename))
        
        # Save to DB
        doc = CandidateDocument(
            candidate_id=current_user.candidate.id,
            filename=filename,
            file_type='Document' # Simplified for now
        )
        db.session.add(doc)
        db.session.commit()
        flash('File uploaded successfully!', 'success')
        
    return redirect(url_for('applicant.dashboard'))

@bp.route('/apply/<int:job_id>')
@login_required
def apply_job(job_id):
    job = JobPosting.query.get_or_404(job_id)
    # Logic to apply for job (e.g., update candidate position or create an application record)
    # For now, just update the candidate's target position
    current_user.candidate.position = job.title
    db.session.commit()
    flash(f'Successfully applied for {job.title}!', 'success')
    return redirect(url_for('applicant.dashboard'))
