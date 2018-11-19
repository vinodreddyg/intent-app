from flask import Blueprint, request, current_app, jsonify
from .dp_model import DPModel
from app.intentcloud import register_intent

mod = Blueprint('deeppavlov', __name__)
_models = {}

def get_model():
	intent_config_path = current_app.config['DP_INTENT_CONFIG_PATH']
	ner_config_path = current_app.config['DP_NER_CONFIG_PATH']
	keys = (intent_config_path, ner_config_path)
	if _models.get(keys, None) == None:
		_models[keys] = DPModel(intent_config_path, ner_config_path)
	return _models[keys]

@mod.route('/parse', methods=['GET', 'POST'])
def parse():
	text = request.args.get('text')
	model = get_model()
	parsed_info = model.parse(text)
	register_intent(parsed_info['intent']['value'])
	return jsonify(parsed_info)

