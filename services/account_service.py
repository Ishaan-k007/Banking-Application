from models.transaction import Transaction
from models.account import AccountTable

from models.user import User 
def get_account_balance(account_id):
    account = AccountTable.query.filter_by(id=account_id).first()
    if account is None:
        return 0.0
    return account.balance

def get_transactions(account_id):
    transactions = Transaction.query.filter_by(id=account_id).all()
    return transactions