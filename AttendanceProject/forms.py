from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,ValidationError
from flask_wtf.file import FileField, FileAllowed
from AttendanceProject.models import User
from flask_login import current_user

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Log in')

class DashBoard(FlaskForm):
    first_name= StringField('Email',validators=[DataRequired()])
    last_name= StringField('Email',validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired(),Email()])