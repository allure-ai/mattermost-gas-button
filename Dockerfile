FROM registry.gitlab.com/allure-ai/docker-images/flask-gunicorn:latest

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

ADD ./app /app/app

EXPOSE 8000
