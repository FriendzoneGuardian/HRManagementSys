from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    print("Resetting passwords...")
    
    admin = User.query.filter_by(username='admin').first()
    if admin:
        admin.set_password('admin123')
        print("Admin password reset to 'admin123'")
    
    hr = User.query.filter_by(username='hr').first()
    if hr:
        hr.set_password('hr123')
        print("HR password reset to 'hr123'")
        
    db.session.commit()
    print("Passwords committed.")
