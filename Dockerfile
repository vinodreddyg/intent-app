FROM python:3.6

RUN apt-get update \
	apt-get install -y g++

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ONBUILD COPY requirements.txt /usr/src/app/
ONBUILD RUN pip install --no-cache-dir -r requirements.txt

ONBUILD COPY . /usr/src/app

CMD ["python", "-m", "spacy", "download", "en"]

EXPOSE 5000

CMD ["python", "./intent_app.py"]

