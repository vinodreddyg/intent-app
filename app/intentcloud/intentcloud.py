from wordcloud import WordCloud
from app import mongo

class IntentCloud():
	def __init__(self):
		return

	def register_intent(self, intent):
		query = {'intent': intent}
		obj = mongo.db.intent_frequencies.find_one(query)
		update_freq = 1 if obj == None else obj.get('frequency', 0) + 1
		mongo.db.intent_frequencies.update_one(query, {
			'$set':{
				'intent': intent,
				'frequency': update_freq
			}},upsert=True)

	def generate_cloud(self):
		freq_dict = self.get_intent_freqs()
		wc = WordCloud(background_color="white", max_words=1000)
		wc.generate_from_frequencies(freq_dict)
		return wc.to_image()

	def get_intent_freqs(self):
		intent_freqs = {}
		cursor = mongo.db.intent_frequencies.find({})
		for doc in cursor:
			intent_freqs[doc['intent']] = doc['frequency']
		return intent_freqs
