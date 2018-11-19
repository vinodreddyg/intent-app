from flask import Blueprint, request, current_app, jsonify
from .rasa_model import RasaModel
from app.intentcloud import register_intent

mod = Blueprint('rasanlu', __name__)
_models = {}

def get_model():
	model_path = current_app.config['RASA_MODEL_PATH']
	if _models.get(model_path, None) == None:
		_models[model_path] = RasaModel(model_path)
	return _models[model_path]

@mod.route('/parse', methods=['GET', 'POST'])
def parse():
	text = request.args.get('text')
	model = get_model()
	parsed_info = model.parse(text)
	register_intent(parsed_info['intent']['value'])
	return jsonify(parsed_info)

	
