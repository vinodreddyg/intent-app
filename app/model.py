from .rasanlu.rasa_model import RasaModel
from .deeppavlov.dp_model import DPModel
from .intentcloud import IntentCloud
from .snipsnlu import SnipsModel

rasa_model = RasaModel()
intent_cloud = IntentCloud()

DP_CONFIG_PATH = './app/deeppavlov/config/intent_snips_big.json'
dp_model = DPModel(DP_CONFIG_PATH, download=True)

SNIPS_CONFIG_PATH = './app/snipsnlu/config/snips_sample'
snips_model = SnipsModel(SNIPS_CONFIG_PATH)


