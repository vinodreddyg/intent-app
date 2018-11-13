from snips_nlu import SnipsNLUEngine, load_resources

class SnipsModel():
	def __init__(self, config_path):
		self.engine = SnipsNLUEngine.from_path(config_path)

	def parse(self, text):
		return self.parse_model_response(self.engine.parse(text))

	def parse_model_response(self, response):
		intent = {
			'value': response['intent']['intentName'],
			'score': response['intent']['probability']
		}
		response['intent'] = intent
		return response