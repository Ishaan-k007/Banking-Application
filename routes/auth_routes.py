from flask import Blueprint, request, render_template, redirect, url_for,flash
from flask_login import login_user, logout_user, current_user

from models import db
from services.auth_service import RegisterForm,LoginForm
from models.user import User
from flask_bcrypt import bcrypt

auth = Blueprint('auth', __name__) # how does this whole blueprint system work?
# can now accept GET AND POST REQUESTS
@auth.route('/register' , methods = ['GET','POST'])
def registers():
    # flashed messages must also be shown in html file
    # data has access to form within route
    if request.method == "POST":
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        
        if len(username) <4:
            flash('username must be greater than 4 characters', category = 'error')
        elif len(password1) < 4:
            flash('password must be greater than 4 characters', category = 'error')
        elif password1 != password2:
            flash('passwords dont match', category = 'error')
        else:
            flash('Account created!', category = 'success')
            new_user = User(username = username, password = password1)
            db.session.add(new_user)
            db.session.commit()
        
   
    #register_form = RegisterForm()
    #new_user = None
 
    #if register_form.validate_on_submit():
    
    # need to initialise the account in the users database
        
        # check length of user database - user id = length + 1  - automatically does it
        # username + password from form
    # need to link the user to an account 
    # need to give access to user dashboard
    return render_template('register.html')



# authentication
@auth.route('/login' , methods = ['GET','POST'])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
    
        user = User.query.filter_by(username=username).first()
        if user != None:
            if user.password == password:
                flash("Accepted Username and Password!", category = 'success')
                login_user(user)
                return redirect(url_for("user.view_account")) ## do this instead of rendering template to change url and match methods
            else:
                flash("Password not correct!", category = "error")
                return render_template('login.html')
        else:
            flash("Username not found!", category = "error")
            return render_template('login.html')
    return render_template('login.html')
    
   