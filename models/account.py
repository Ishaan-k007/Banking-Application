from models import db  # this imports the code that can generate a database
from flask_login import UserMixin # what does this do?
from models.user import User
from sqlalchemy import ForeignKey
class AccountTable(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable=False, unique=True)
    balance = db.Column(db.Float, nullable=False, default=0.0)
    User_id = db.Column(db.Integer, db.ForeignKey("User.id"))
    interest_rate = db.Column(db.Integer, nullable = False)
    