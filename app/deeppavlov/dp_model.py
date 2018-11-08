from deeppavlov.core.commands.infer import build_model_from_config
from deeppavlov.download import deep_download

class DPModel():
	def __init__(self, config_path, download=False):
		if download == True:
			deep_download(config_path)
		model = build_model_from_config(config_path)

	def parse(text):
		return model([text])