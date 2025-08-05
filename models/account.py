from models import db  # this imports the code that can generate a database
from flask_login import UserMixin # what does this do?
from models.user import User
from sqlalchemy import ForeignKey
class AccountTable(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable=False, unique=True)
    account_name = db.Column(db.String(40), nullable = False, unique = True )
    balance = db.Column(db.Float, nullable=False, default=0.0)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    interest_rate = db.Column(db.Integer, nullable = False,default = 0.1)
    transactions_sent = db.relationship(
    "Transaction",
    foreign_keys='Transaction.sender_account_id',
    backref='sender_account',
    lazy="dynamic")

    transactions_received = db.relationship(
    "Transaction",
    foreign_keys='Transaction.reciever_account_id',
    backref='receiver_account',
    lazy="dynamic")
    