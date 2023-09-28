# DOCKERFILE
FROM python:alpine

COPY requirements.txt /app

RUN pip install -r /app/requirements.txt

COPY . /app

WORKDIR /app

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
