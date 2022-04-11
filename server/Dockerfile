FROM python:3.9-slim

RUN apt-get update

WORKDIR /painting_style_classificator/server

COPY . /painting_style_classificator/server

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 5000
