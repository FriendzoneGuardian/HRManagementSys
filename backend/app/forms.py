from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, FloatField
from wtforms.validators import DataRequired, Email, Length, ValidationError
from app.models import Department

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class CandidateForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=64)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=64)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    position = StringField('Position', validators=[DataRequired(), Length(max=64)])
    department = SelectField('Department', coerce=int, validators=[DataRequired()])
    expected_salary = FloatField('Expected Salary', validators=[DataRequired()])
    status = SelectField('Status', choices=[
        ('Applied', 'Applied'),
        ('Interviewing', 'Interviewing'),
        ('Offer', 'Offer'),
        ('Rejected', 'Rejected')
    ], validators=[DataRequired()])
    submit = SubmitField('Submit')

    def __init__(self, *args, **kwargs):
        super(CandidateForm, self).__init__(*args, **kwargs)
        self.department.choices = [(d.id, d.name) for d in Department.query.all()]
