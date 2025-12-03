from app import create_app, db
from app.models import User

app = create_app()
with app.app_context():
    print("--- Debugging Users ---")
    users = User.query.all()
    for u in users:
        print(f"User: {u.username}, Role: {u.role}, Hash: {u.password_hash[:10]}...")
    
    admin = User.query.filter_by(username='admin').first()
    if admin:
        print(f"Admin found. Hash: {admin.password_hash}")
        print("Attempting to verify 'admin123'...")
        if admin.check_password('admin123'):
            print("SUCCESS: Password 'admin123' is VALID.")
        else:
            print("FAILURE: Password 'admin123' is INVALID.")
            
            print("--- RESETTING PASSWORD ---")
            admin.set_password('admin123')
            db.session.commit()
            print(f"New Hash: {admin.password_hash}")
            
            if admin.check_password('admin123'):
                print("SUCCESS: Password 'admin123' is VALID after reset.")
            else:
                print("FAILURE: Password 'admin123' is STILL INVALID after reset.")
    else:
        print("FAILURE: Admin user not found.")
