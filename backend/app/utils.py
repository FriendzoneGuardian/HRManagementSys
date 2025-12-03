from app import db
from app.models import AuditLog
from flask_login import current_user

def log_user_action(action, details=None):
    if current_user.is_authenticated:
        log = AuditLog(user_id=current_user.id, action=action, details=details)
        db.session.add(log)
        db.session.commit()
