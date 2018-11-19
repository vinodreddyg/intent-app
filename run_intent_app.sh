brew install mongodb
mkdir -p /data/db
sudo chown $USER:$USER /data/db
brew services start mongodb
pip install -r requirements.txt
python -m snips_nlu download en
python -m deeppavlov download app/deeppavlov/config/intents_snips_big.json
python -m deeppavlov download app/deeppavlov/config/ner_conll2003.json
export FLASK_ENV=development
export FLASK_APP=intent_app.py
flask run