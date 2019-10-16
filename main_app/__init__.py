from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db.sqlite3'
marshmallow = Marshmallow(app)

db = SQLAlchemy(app)

from main_app.routes import person_api

db.create_all()