from app import create_app, db
from app.models import User

app = create_app()

def check_user(username, password, role):
    user = User.query.filter_by(username=username).first()
    if not user:
        print(f"[-] User {username} NOT FOUND")
        return False
    
    if user.role != role:
        print(f"[-] User {username} has wrong role: {user.role} (expected {role})")
        return False
        
    if not user.is_approved:
        print(f"[-] User {username} is NOT APPROVED")
        return False
        
    if not user.check_password(password):
        print(f"[-] User {username} has INVALID PASSWORD")
        return False
        
    print(f"[+] User {username} ({role}) - OK")
    return True

with app.app_context():
    print("--- Verifying Test Accounts ---")
    check_user('admin', 'admin123', 'Admin')
    check_user('hr', 'hr123', 'HR')
    check_user('candidate0@example.com', 'password123', 'Applicant')
    check_user('candidate1@example.com', 'password123', 'Applicant')
    print("--- Verification Complete ---")
