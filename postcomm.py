from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'teste123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///postcomm.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
