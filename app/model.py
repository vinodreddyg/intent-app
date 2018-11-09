from .rasanlu.rasa_model import RasaModel
# from .deeppavlov.dp_model import DPModel
from .intentcloud import IntentCloud

model = RasaModel()
intent_cloud = IntentCloud()

print(type(intent_cloud))


# DP_CONFIG_PATH = './app/deeppavlov/config/intent_snips_big.json'
# model = DPModel(DP_CONFIG_PATH, download=True)




