FROM theskyvalker/cv2-tf-keras-py38

WORKDIR .

COPY . .

CMD [ "python3", "app.py"]
