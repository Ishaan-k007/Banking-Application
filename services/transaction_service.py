from models.transaction import Transaction
from models.account import AccountTable
from models import db 

def add_transaction(sender_account_id,reciever_account_id,Date, Amount):
    new_transaction = Transaction(sender_account_id=sender_account_id, Date=Date, Amount=Amount, reciever_account_id=reciever_account_id)
    db.session.add(new_transaction)
    db.session.commit()

def update_account_balance(account_id, amount):
    account = AccountTable.query.filter_by(account_id=account_id).first()
    if account:
        account.balance += amount
    else:
        Transaction(Status = "Failed")
