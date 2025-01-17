from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import login_user, logout_user
from services.auth_service import create_user, authenticate_user
from models import db
from services.auth_service import RegisterForm,LoginForm
from models.user import User
from flask_bcrypt import bcrypt

auth_routes = Blueprint('auth', __name__) # how does this whole blueprint system work?
@auth_routes.route('/register' , methods = ['GET','POST'])
def create_new_user():
    RegisterForm()
    # need to give access to dashboard
    return redirect(url_for('dashboard'))



# authentication
def authenticate_a_known_user():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)