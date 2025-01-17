from models import db  # this imports the code that can generate a database
from flask_login import UserMixin # what does this do?
class User(db.Model, UserMixin):  # Creates the database with columns
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)