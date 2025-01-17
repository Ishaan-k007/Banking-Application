from models import db  # this imports the code that can generate a database
from flask_login import UserMixin,For # what does this do?
from models.user import User
from sqlalchemy import ForeignKey
class AccountTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, ForeignKey(User.id, ondelete='CASCADE'), nullable=False, unique=True)
    balance = db.Column(db.Float, nullable=False, default=0.0)
