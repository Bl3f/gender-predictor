FROM python:3.10

RUN apt-get update

WORKDIR /app
ADD ./requirements.txt requirements.txt

RUN pip install -r requirements.txt

ADD model.v1.pickle model.v1.pickle
ADD main.py main.py

CMD ["python", "main.py"]