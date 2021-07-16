FROM python:3.8-slim-buster

WORKDIR .

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y && apt-get autoremove && apt-get clean

CMD [ "python3", "app.py"]