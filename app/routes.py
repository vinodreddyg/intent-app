from app import app
from flask import request, g, jsonify, send_file
import io
from .intentcloud import generate_cloud
	
@app.route('/intentcloud', methods=['GET'])
def get_intent_cloud():
	img = generate_cloud()
	output = io.BytesIO()
	img.convert('RGBA').save(output, format='PNG')
	output.seek(0, 0)
	return send_file(output, mimetype='image/png', as_attachment=False)
