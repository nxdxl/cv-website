# DOCKERFILE
FROM python:alpine

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
