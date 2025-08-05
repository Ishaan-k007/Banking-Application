from flask import Flask, render_template, redirect, url_for,request
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from sqlalchemy import ForeignKey
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import bcrypt
from models.account import AccountTable

# creates account form

    