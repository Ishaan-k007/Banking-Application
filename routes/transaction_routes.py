from flask import Blueprint, request, render_template
from flask_login import login_required, current_user
from services.transaction_service import add_transaction, 
from models import db
from models.transaction import Transaction
from models.account import AccountTable

transaction_routes = Blueprint('transactions', __name__)

@transaction_routes.route('/add', methods=['POST'])
@login_required  ##### how does this work / how does it know I am logged in

# displays transaction page 
# asks what you want to do 
# imports functions from the services 
# does it.  