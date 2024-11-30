from flask import render_template,url_for,flash,redirect,request,abort
from AttendanceProject import app,db,mail
from AttendanceProject.models import User,Courses
from flask_login import login_user,logout_user,current_user,login_required
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Message
from werkzeug.utils import secure_filename
from AttendanceProject.forms import LoginForm

@app.route("/")
@app.route("/home",methods=["GET"])
def home():
    return render_template("home.html",title="Home Page")

@app.route('/login',methods=["GET","POST"])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password,password):
            login_user(user, remember=True)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Incorrect email or password.','danger')
    return render_template('login.html',form=form)

@app.route('/logout',methods=["GET"])
def logout():
    if current_user.is_authenticated:
        logout_user()
        return redirect(url_for('home'))
    else:
        flash('You are already logged out.','info')
        return redirect(url_for('home'))
    return redirect(url_for('home'))

@app.route('/profile',methods=["GET"])
@login_required
def profile():
    name = current_user.first_name
    return render_template('profile.html',title=f'{name} Dashboard')