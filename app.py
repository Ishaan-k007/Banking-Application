from flask import Flask, render_template 
from flask_login import LoginManager
from config import Config
from models import db
from models.user import User
from routes.auth_routes import auth
from routes.account_routes import account
from routes.user_routes import user
from routes.transaction_routes import transaction

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)


# Initialize LoginManager
login_manager = LoginManager() 
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id: str):
    """ Returns a userID for Flask-Login, or None if the user does not exist. """
    try:
        uid = int(user_id)
    except (ValueError, TypeError):
        return None
    return User.query.get(uid)

# Initialise a database 
db.init_app(app)


# Register blueprints
app.register_blueprint(auth, url_prefix='/')
app.register_blueprint(account, url_prefix='/')
app.register_blueprint(user, url_prefix='/')
app.register_blueprint(transaction, url_prefix = "/")

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
