from deeppavlov.core.commands.infer import build_model_from_config
from deeppavlov.download import deep_download
from .dp_base import DPBase

class DPModel():
	def __init__(self, intent_path, ner_path):
		self.ner_model = DPBase(ner_path, download=False)
		self.intent_model = DPBase(intent_path, download=False)

	def parse(self, text):
		intents = self.parse_intent_response(self.intent_model.parse(text))
		entities = self.parse_ner_response(self.ner_model.parse(text))
		resp = {'text': text}
		resp.update(intents)
		resp.update(entities)
		return resp

	def parse_intent_response(self, response):
		# return {
		#   'intents': [
		# 		{
		# 			'value': intent,
		# 			'score': score
		#		}
		#.   ]
		# }
		sorted_intents = sorted(response[0].items(), key=lambda x: x[1])
		sorted_intent_hash = [{'value': k, 'score': v} for k,v in sorted_intents]
		return {
			'intent': sorted_intent_hash[0],
			'intent_ranking': sorted_intent_hash
		}

	def parse_ner_response(self, response):
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

		tokens, tags = response[0][0], response[1][0]
		entities = [{ 'value': tokens[i], 'entity': tags[i] } for i in range(len(tokens)) if not tags[i] == 'O']
		return {
			'entities': entities
		}
