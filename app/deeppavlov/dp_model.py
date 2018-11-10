from deeppavlov.core.commands.infer import build_model_from_config
from deeppavlov.download import deep_download
from .dp_base import DPBase

class DPModel():
	def __init__(self, intent_path, ner_path):
		ner_model = DPBase(ner_path, download=True)
		intent_model = DPBase(intent_path, download=True)

	def parse(text):
		intents = parse_intent_response(intent_model([text]))
		entities = parse_ner_response(ner_model([text]))
		resp = {'text': text}
		resp.update(intents)
		resp.update(entities)
		return resp

	def parse_intent_response(response):
		# return {
		#   'intents': [
		# 		{
		# 			'value': intent,
		# 			'score': score
		#		}
		#.   ]
		# }
		intents = sorted(response.items(), key=lambda x: x[1])
		intents = [{'value': k, 'score': v} for k,v in response]
		return {
			'intents': intents
		}

	def parse_ner_response(response):
		# return {
		# 	'entities': [
		# 		{
		# 			'value': value,
		# 			'entity': entity,
		# 			'entity_start': entity_start,
		# 			'entity_end': entity_end
		# 		}
		# 	]
		# }

		tokens, tags = response
		entities = [{ 'value': tokens[i], 'entity': tags[i] } for i in range(len(tokens)) if not tags[i] == 'O']
		return {
			'entities': entities
		}
