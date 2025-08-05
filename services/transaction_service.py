from models.transaction import Transaction
from models.account import AccountTable
from models import db 
from flask import flash
def add_transaction(sender_account_id,reciever_account_id,Date, Amount):
    new_transaction = Transaction(sender_account_id=sender_account_id, Date=Date, Amount=Amount, reciever_account_id=reciever_account_id)
    db.session.add(new_transaction)
    db.session.commit()

def update_account_balance(sender_account,reciever_account, amount):
    if sender_account:
        print(sender_account)
        sender_account.balance -= int(amount)
        print(sender_account.balance)
        db.session.commit()
        flash("Success", category = "success")
        
    else:
        Transaction(Status = "Failed")
        flash("Error", category = "error")
    if reciever_account:
        #print(reciever_account)
        reciever_account.balance += int(amount)
        db.session.commit()
        flash("Success", category = "success")
    else:
        Transaction(Status = "Failed")
        flash("Error", category = "error")
            