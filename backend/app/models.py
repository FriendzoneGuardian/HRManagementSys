from app import db, login
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), default='Applicant') # Admin, HR, Applicant
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidate.id'), nullable=True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password, method='pbkdf2:sha256')
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
        
    def __repr__(self):
        return f'<User {self.username}>'

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    candidates = db.relationship('Candidate', backref='department', lazy='dynamic')

    def __repr__(self):
        return f'<Department {self.name}>'

class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), index=True)
    last_name = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    position = db.Column(db.String(64))
    application_date = db.Column(db.DateTime, default=datetime.utcnow)
    expected_salary = db.Column(db.Float)
    status = db.Column(db.String(32), default='Applied') # Applied, Interviewing, Offer, Rejected
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    user = db.relationship('User', backref='candidate', uselist=False)
    
class AuditLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    action = db.Column(db.String(64), nullable=False)
    details = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('audit_logs', lazy=True))

    def __repr__(self):
        return f'<AuditLog {self.action} by User {self.user_id}>'
