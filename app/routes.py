from app import app
from flask import request, g, jsonify, send_file
from .model import rasa_model, intent_cloud, snips_model
import io
	
@app.route('/parse-rasa', methods=['GET', 'POST'])
def parse_rasa():
	text = request.args.get('text')
	if rasa_model is None:
		return jsonify({'Error': 'Rasa parsing disabled'})
	else:
		return parse_model(rasa_model, text)

@app.route('/parse-dp', methods=['GET', 'POST'])
def parse_rasa():
	text = request.args.get('text')
	if dp_model is None:
		return jsonify({'Error': 'Deep Pavlov parsing disabled'})
	else:
		return parse_model(dp_model, text)

@app.route('/parse-snips', methods=['GET', 'POST'])
def parse_rasa():
	text = request.args.get('text')
	if snips_model is None:
		return jsonify({'Error': 'Snips parsing disabled'})
	else:
		return parse_model(snips_model, text)

@app.route('/intentcloud', methods=['GET'])
def get_intent_cloud():
	img = intent_cloud.generate_cloud()
	output = io.BytesIO()
	img.convert('RGBA').save(output, format='PNG')
	output.seek(0, 0)
	return send_file(output, mimetype='image/png', as_attachment=False)

def parse_model(model, text):
	parsed_info = model.parse(text)
	intent_cloud.register_intent(parsed_info['intent']['value'])
	return jsonify(parsed_info)
