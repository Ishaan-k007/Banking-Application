from models.transaction import Transaction
from models.account import AccountTable

from models.user import User 
def get_account_balance(user_id):
    account = AccountTable.query.filter_by(account_id=user_id).first()
    if account is None:
        return 0.0
    return account.balance

def get_transactions(user_id):
    transactions = Transaction.query.filter_by(account_id=user_id).all()
    return transactions