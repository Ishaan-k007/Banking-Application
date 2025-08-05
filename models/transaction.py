from models import db  # this imports the code that can generate a database
from flask_login import UserMixin # what does this do?
from sqlalchemy import ForeignKey
from models.user import User
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_account_id = db.Column(db.Integer, db.ForeignKey('account_table.id'))
    reciever_account_id = db.Column(db.Integer, db.ForeignKey('account_table.id'))
    Amount = db.Column(db.Float, nullable = False)
    Date = db.Column(db.String)
    Status = db.Column(db.String)