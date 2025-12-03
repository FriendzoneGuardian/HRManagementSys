from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = 'Please log in to access this page.'

def create_app(config_class=Config):
    app = Flask(__name__, 
                template_folder='../../frontend/templates',
                static_folder='../../frontend/static')
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    from app import routes, models, auth
    app.register_blueprint(routes.bp)
    app.register_blueprint(auth.bp)

    return app
