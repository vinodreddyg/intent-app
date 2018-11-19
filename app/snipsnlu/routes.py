from flask import Blueprint, request, current_app, jsonify
from .snips_model import SnipsModel
from app.intentcloud import register_intent

mod = Blueprint('snipsnlu', __name__)
_models = {}

def get_model():
	model_path = current_app.config['SNIPS_MODEL_PATH']
	if _models.get(model_path, None) == None:
		_models[model_path] = SnipsModel(model_path)
	return _models[model_path]

@mod.route('/parse', methods=['GET', 'POST'])
def parse():
	text = request.args.get('text')
	model = get_model()
	parsed_info = model.parse(text)
	intent = parsed_info['intent']['value']
	if intent is not None:
		register_intent(intent)
	return jsonify(parsed_info)

