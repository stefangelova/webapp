from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
app.config.from_object(Config)
app.config['SQL_ALCHEMY_DATABASE_URI'] = str(os.getenv('DATABASE_URI'))

from app import routes, models
