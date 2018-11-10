from flask import Flask, g
from .rasanlu.rasa_model import RasaModel
from flask_pymongo import PyMongo
from .deeppavlov import DPModel, Proba2Dict

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/intentDb"
mongo = PyMongo(app)

from app import routes