from snips_nlu import SnipsNLUEngine, load_resources

class SnipsModel():
	def __init__(self, model_path):
		self.engine = SnipsNLUEngine.from_path(model_path)

	def parse(self, text):
		return self.parse_model_response(self.engine.parse(text))

	def parse_model_response(self, response):
		if response['intent'] == None:
			intent = {'value': None, 'score': 0}
		else:
			intent = {
				'value': response['intent'].get('intentName', None),
				'score': response['intent'].get('probability', 0)
			}
		response['intent'] = intent
		return response