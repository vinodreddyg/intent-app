from flask import Flask, g
from .rasanlu.rasa_model import RasaModel
from flask_pymongo import PyMongo
from .deeppavlov import DPModel, Proba2Dict

app = Flask(__name__)
app.config.from_object('config')
mongo = PyMongo(app)

from app.rasanlu.routes import mod
app.register_blueprint(rasanlu.routes.mod, url_prefix='/rasanlu')

from app.snipsnlu.routes import mod
app.register_blueprint(snipsnlu.routes.mod, url_prefix='/snipsnlu')

from app.deeppavlov.routes import mod
app.register_blueprint(deeppavlov.routes.mod, url_prefix='/deeppavlov')

from app import routes