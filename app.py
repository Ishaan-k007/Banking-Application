from flask import Flask
from config import Config
from models import db
from routes import auth_routes, transaction_routes, account_routes

app = Flask(__name__)
#
app.config.from_object(Config)

# Initialise a database 
db.init_app(app)

# Register blueprints - 
app.register_blueprint(auth_routes, url_prefix='/auth')
app.register_blueprint(transaction_routes, url_prefix='/transactions')
app.register_blueprint(account_routes, url_prefix='/accounts')

if __name__ == '__main__':
    app.run(debug=True)