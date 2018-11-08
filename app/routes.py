from app import app
from flask import request, g, jsonify
from .model import model, word_cloud_service

@app.route('/')
@app.route('/index')
def index():
	return 'Hello'


@app.route('/parse', methods=['GET', 'POST'])
def parse():
	text = request.args.get('text')
	parsed_info = model.parse(text)
	return jsonify(parsed_info)


@app.route('/intentcloud', methods=['GET'])
def intent_cloud():
	return