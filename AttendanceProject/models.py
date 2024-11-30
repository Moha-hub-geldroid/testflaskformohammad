from AttendanceProject import app,db,login_manager
from flask_login import UserMixin
from itsdangerous import URLSafeTimedSerializer as serelizer

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(16),nullable=False)
    last_name = db.Column(db.String(16),nullable=False)
    email = db.Column(db.String(50),nullable=False,unique=True)
    password = db.Column(db.String(60),nullable=False)
    courses = db.relationship('Courses', backref='user', lazy=True)

class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)