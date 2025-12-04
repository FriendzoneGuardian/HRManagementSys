
"""
Clarion HRMS - Application Factory
==================================
Purpose:
    Initializes the Flask application, configures extensions (SQLAlchemy, Migrate, Login, CSRF),
    and registers blueprints.

Key Components:
    - create_app(): Factory function to create Flask app instance.
    - db: SQLAlchemy instance.
    - login: LoginManager instance.
    - csrf: CSRFProtect instance.

Author: Antigravity AI
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from config import Config

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = 'Please log in to access this page.'
csrf = CSRFProtect()

def create_app(config_class=Config):
    app = Flask(__name__, 
                template_folder='../../frontend/templates',
                static_folder='../../frontend/static')
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    csrf.init_app(app)

    from app import routes
    app.register_blueprint(routes.bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    from app.applicant import bp as applicant_bp
    app.register_blueprint(applicant_bp, url_prefix='/applicant')
    
    @app.context_processor
    def inject_now():
        from datetime import datetime
        return {'now': datetime.now}

    return app
