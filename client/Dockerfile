FROM python:3.9-slim

RUN apt-get update

WORKDIR /painting_style_classificator/client

COPY . /painting_style_classificator/client

RUN pip install --no-cache-dir --upgrade -r requirements.txt