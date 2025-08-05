from flask import Blueprint, request, render_template
from flask_login import login_required, current_user
from services.transaction_service import add_transaction,update_account_balance
from models import db
from models.transaction import Transaction
from models.account import AccountTable
from flask import flash

transaction = Blueprint('transaction', __name__)

@transaction.route('/view/<int:account_id>', methods=['GET','POST'])
@login_required ##### how does this work / how does it know I am logged in

def make_transactions(account_id):
    
    
    sender_account = AccountTable.query.filter_by(id = account_id).first()
    
    if request.method == "POST":
        reciever_account_name = request.form.get("reciever_account_name")
        amount = request.form.get("amount")
        date = request.form.get("date")
        reciever_account = AccountTable.query.filter_by(account_name = reciever_account_name).first() # .first() is important to add why?

        if reciever_account:
            add_transaction(sender_account.id,reciever_account.id,date, amount)
            update_account_balance(sender_account,reciever_account, amount)
        else:
            flash("Error", category = "error")
    
    return render_template("Transactions.html")
    
    
    


@transaction.route('/view/<int:account_id>', methods=['GET','POST'])
@login_required

def view_transactions(account_id):
    print("Hiu")
    account = AccountTable.query.filter_by(id = account_id).first()
    if not account:
        print("404")
    sent_transactions = account.transactions_sent.all()
    received_transactions = account.transactions_received.all()
    print(sent_transactions)
    print(received_transactions)
  
    return render_template('Transactions.html', account = account, sent_transactions = sent_transactions, received_transactions = received_transactions)