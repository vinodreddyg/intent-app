from deeppavlov.core.commands.infer import build_model_from_config
from deeppavlov.download import deep_download

class DPBase():
	def __init__(self, config_path, download=False):
		if download == True:
			deep_download(config_path)
		self.model = build_model_from_config(config_path)

	def parse(self, text):
		return self.model([text])