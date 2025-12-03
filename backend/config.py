import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    if not SECRET_KEY:
        SECRET_KEY = 'dev-default-secret-key'
        print("WARNING: SECRET_KEY not set in .env. Using insecure default.")

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    if not SQLALCHEMY_DATABASE_URI:
        SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/hr_management_sys'
        print("WARNING: DATABASE_URL not set in .env. Using default XAMPP connection.")

    SQLALCHEMY_TRACK_MODIFICATIONS = False
