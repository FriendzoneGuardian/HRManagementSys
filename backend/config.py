import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # XAMPP default credentials: user=root, password=empty, host=localhost, port=3306
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://root:@localhost:3306/hr_management_sys'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
