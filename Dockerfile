FROM python:3.7.3
MAINTAINER Borja Erice <erice.borja@hotmail.com>

RUN groupadd flaskgroup && useradd -m -g flaskgroup -s /bin/bash flask

RUN mkdir -p /home/flask/app/characters_microservice
WORKDIR /home/flask/app/characters_microservice

COPY requirements.txt /home/flask/app/characters_microservice
RUN pip install --no-cache-dir -r requirements.txt

COPY . /home/flask/app/characters_microservice

RUN chown -R flask:flaskgroup /home/flask

USER flask
