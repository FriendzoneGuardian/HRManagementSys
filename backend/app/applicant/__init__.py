from flask import Blueprint

bp = Blueprint('applicant', __name__)

from app.applicant import routes
