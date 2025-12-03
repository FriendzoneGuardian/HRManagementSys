from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    users = User.query.all()
    print(f"Total Users: {len(users)}")
    for u in users:
        print(f"User: {u.username}, Role: {u.role}, Approved: {u.is_approved}")
        
    admin = User.query.filter_by(username='admin').first()
    if admin:
        print(f"Admin Password Hash: {admin.password_hash}")
    else:
        print("Admin user not found!")
