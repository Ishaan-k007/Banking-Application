# allows for creation of account
# allows to view and select account
# needs current user
from flask import Blueprint, request, render_template, redirect, url_for


from models import db
from flask_login import login_user,current_user
from models.user import User
from models.account import AccountTable
from flask_bcrypt import bcrypt

user = Blueprint('user', __name__) # how does this whole blueprint system work?
@user.route('/view_account', methods = ['GET', 'POST'])
def view_account():
    

    account_info = AccountTable.query.filter_by(user_id=current_user.id).all()
    print("Hi",account_info)
    return render_template('UserDashboard.html', accounts=account_info)

@user.route('/create_account', methods = ['GET', 'POST'])
def create_account():
    
    if request.method == "POST":
        account_name = request.form.get("account_name")
        accounts = AccountTable.query.filter_by(user_id = current_user.id).all()
        account_db_name = [account.account_name for account in accounts]
        if account_name not in account_db_name:
            new_account = AccountTable(account_name = account_name, user_id = current_user.id)
            db.session.add(new_account)
            db.session.commit()
            
            return render_template('UserDashboard.html') ## this is the switched base template
    return render_template("create_account.html") ## this is base render template