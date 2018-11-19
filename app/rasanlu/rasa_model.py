from rasa_nlu.model import  Metadata, Interpreter

class RasaModel():
	def __init__(self, model_path):
		self.model = Interpreter.load(model_path)

	def parse(self, text):
		return self.parse_model_response(self.model.parse(text))

	def parse_model_response(self, response):
		parsed_resp = {
			'text': response['text']
		}
		intent = {
			'value': response['intent']['name'],
			'score': response['intent']['confidence']
		}
		intents = [{
			'value': intent['name'],
			'score': intent['confidence']
		} for intent in response['intent_ranking']]
		entities = [{
			'value': entity['value'],
			'entity': entity['entity'],
			'start': entity['start'],
			'end': entity['end']
		} for entity in response['entities']]
		parsed_resp.update({'intents': intents, 'entities': entities, 'intent': intent})
		return parsed_resp

