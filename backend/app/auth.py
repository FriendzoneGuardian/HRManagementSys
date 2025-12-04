"""
Clarion HRMS - Authentication Routes
====================================
Purpose:
    Manages user session lifecycle: Login, Registration, and Logout.
    Handles user creation and initial role assignment.

Key Routes:
    - /login: User sign-in.
    - /register: New account creation (Applicant/HR/Admin).
    - /logout: Session termination.

Author: Antigravity AI
"""

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from urllib.parse import urlparse
from app import db
from app.models import User, Candidate
from app.forms import LoginForm, RegistrationForm

bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    
    form = LoginForm()
    if form.validate_on_submit():
        print(f"Login attempt: {form.username.data}")
        user = User.query.filter_by(username=form.username.data).first()
        
        if user is None or not user.check_password(form.password.data):
            print("Invalid username or password")
            flash('Invalid username or password', 'error')
            return redirect(url_for('auth.login'))
        
        if not user.is_approved:
            print("User not approved")
            flash('Your account is pending approval. Please contact the administrator.', 'warning')
            return redirect(url_for('auth.login'))
        
        print(f"Login success: {user.username} ({user.role})")
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlparse(next_page).netloc != '':
            next_page = url_for('main.dashboard')
        return redirect(next_page)
    elif request.method == 'POST':
        print(f"Form validation failed: {form.errors}")
        
    return render_template('login.html', title='Sign In', form=form)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, role=form.role.data, is_approved=False)
        user.set_password(form.password.data)
        
        if form.role.data == 'Applicant':
            candidate = Candidate(
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                email=form.username.data,
                status='Applied'
            )
            db.session.add(candidate)
            user.candidate = candidate
        
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now registered! Your account is pending approval.', 'success')
        return redirect(url_for('auth.login'))
        
    return render_template('register.html', title='Register', form=form)

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
