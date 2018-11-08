from .rasanlu.rasa_model import RasaModel
from .deeppavlov.dp_model import DPModel
from .wordcloud import WordCloudService

model = RasaModel()
word_cloud_service = WordCloudService()


# DP_CONFIG_PATH = './app/deeppavlov/config/intent_snips_big.json'
# model = DPModel(DP_CONFIG_PATH, download=True)




