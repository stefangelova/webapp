from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
app.config.from_object(Config)
app.config['SQL_ALCHEMY_DATABASE_URI'] = "mysql+pymysql://stef@project1db:Thisisstup1d@project1db.mysql.database.azure.com/proj1db"
db = SQLAlchemy(app)
SQLALCHEMY_TRACK_MODIFICATIONS = False

class User(db.Model):
	__tablename__ = 'users'
	user_id = db.Column('user_id', db.Integer, primary_key=True)
	username = db.Column('username', db.Unicode, index=True, unique=True)
	password = db.Column('password', db.Unicode)
	email = db.Column('email', db.Unicode, index=True, unique=True)
	book_list_id = db.Column('book_list_id', db.Integer) 


