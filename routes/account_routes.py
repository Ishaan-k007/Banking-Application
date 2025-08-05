from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import current_user
from models import db
from services.account_service import get_account_balance,get_transactions
from models.user import User
from models.account import AccountTable
from flask_bcrypt import bcrypt

account = Blueprint('account', __name__)
@account.route('/balance', methods = ['GET', 'POST'])
def view_account_balance():
    account_id = request.args.get('id')  # pulls ?id=1 from the URL
    account = AccountTable.query.filter_by(id = account_id).first()
    account_balance = get_account_balance(account_id)
    return render_template('AccountDashboard.html', balance = account_balance, account = account)


    
    