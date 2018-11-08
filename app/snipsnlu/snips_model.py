from snips_nlu import SnipsNLUEngine, load_resources


class SnipsModel():
	def __init__(self, config_path):
		engine = SnipsNLUEngine.from_path(config_path)

	def parse(self, text):
		return engine.parse(text)