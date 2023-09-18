# DOCKERFILE
FROM ubuntu:22.04

RUN apt update -y && apt install -y sendmail python3 python3-pip

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT python3 app.py
