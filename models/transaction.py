from models import db  # this imports the code that can generate a database
from flask_login import UserMixin # what does this do?
from sqlalchemy import ForeignKey
from models.user import User
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, ForeignKey(User.id, ondelete='CASCADE'), nullable=False)
    date = db.Column(db.String(40), nullable=False)
    payee = db.Column(db.String(40))
    amount = db.Column(db.Float, nullable=False)
    current_balance = db.Column(db.Float, nullable=False)

# What is Foreign Key?
# What is primary key?
# How is this data stored in the computer?
# What is nullable?