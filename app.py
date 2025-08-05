from flask import Flask, render_template  # Add render_template
from flask_login import LoginManager
from config import Config
from models import db
from models.account import AccountTable
from models.transaction import Transaction
from models.user import User

from routes.auth_routes import auth
from routes.account_routes import account
from routes.user_routes import user
from routes.transaction_routes import transaction
from services import account_service, auth_service, transaction_service

app = Flask(__name__)
app.config.from_object(Config)


# Initialize LoginManager
login_manager = LoginManager() ## this is needed for flask login features eg. login_user 
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Initialise a database 
db.init_app(app)
with app.app_context():
    db.create_all()

# Register blueprints
app.register_blueprint(auth, url_prefix='/')
app.register_blueprint(account, url_prefix='/')
app.register_blueprint(user, url_prefix='/')
app.register_blueprint(transaction, url_prefix = "/")

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
