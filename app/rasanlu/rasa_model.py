from rasa_nlu.model import  Metadata, Interpreter

class RasaModel():
	def __init__(self):
		self.model = Interpreter.load('./app/rasanlu/models/nlu/default/chat')

	def parse(self, text):
		return self.model.parse(text)