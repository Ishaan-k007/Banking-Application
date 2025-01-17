from flask import Blueprint, request, render_template
from flask_login import login_required, current_user
from services.transaction_service import add_transaction, get_transactions
from models import db
from models.transaction import Transaction
from models.account import AccountTable

transaction_routes = Blueprint('transactions', __name__)

@transaction_routes.route('/add', methods=['POST'])
@login_required  ##### how does this work / how does it know I am logged in

def add_transaction(account_id, date, payee, amount, current_balance):
    new_transaction = Transaction(account_id=account_id, date=date, amount=amount, payee=payee, current_balance=current_balance)
    db.session.add(new_transaction)
    db.session.commit()

def update_account_balance(account_id, balance):
    account = AccountTable.query.filter_by(account_id=account_id).first()
    if account:
        account.balance = balance
    else:
        new_account = AccountTable(account_id=account_id, balance=balance)
        db.session.add(new_account)
    db.session.commit()