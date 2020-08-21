from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from config import Config


#instantiate flask class
app = Flask(__name__)

app.config.from_object(Config)


#creating db object
db = SQLAlchemy(app)
#createing migrate object
ma = Marshmallow(app)


#seperation of concerns
from app import routes, models
