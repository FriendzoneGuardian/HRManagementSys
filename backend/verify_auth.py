from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    print("Verifying Admin and HR credentials...")
    
    admin = User.query.filter_by(username='admin').first()
    if admin:
        print(f"Admin Hash: {admin.password_hash}")
        print(f"Hash Length: {len(admin.password_hash)}")
        if admin.check_password('admin123'):
            print("SUCCESS: Admin password is correct.")
        else:
            print("FAILURE: Admin password is INCORRECT.")
    else:
        print("FAILURE: Admin user not found.")

    hr = User.query.filter_by(username='hr').first()
    if hr:
        if hr.check_password('hr123'):
            print("SUCCESS: HR password is correct.")
        else:
            print("FAILURE: HR password is INCORRECT.")
    else:
        print("FAILURE: HR user not found.")
