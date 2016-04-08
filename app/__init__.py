from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

from models import *

#TODO
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>'



from app import views, models