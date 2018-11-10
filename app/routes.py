from app import app
from flask import request, g, jsonify, send_file
from .model import model, intent_cloud
import io

@app.route('/parse', methods=['GET', 'POST'])
def parse():
	text = request.args.get('text')
	parsed_info = model.parse(text)
	intent_cloud.register_intent(parsed_info['intent']['name'])
	return jsonify(parsed_info)


@app.route('/intentcloud', methods=['GET'])
def get_intent_cloud():
	img = intent_cloud.generate_cloud()
	output = io.BytesIO()
	img.convert('RGBA').save(output, format='PNG')
	output.seek(0, 0)
	return send_file(output, mimetype='image/png', as_attachment=False)