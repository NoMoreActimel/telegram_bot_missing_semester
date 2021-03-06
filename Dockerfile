# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR ../telegram_bot

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

CMD [ "python3", "main.py", "--host=0.0.0.0"] 
