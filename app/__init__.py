from flask import Flask, g
from .rasanlu.rasa_model import RasaModel
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

from app import routes