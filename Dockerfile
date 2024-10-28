FROM python:3.8
COPY . /app
WORKDIR /app

RUN pip install flask

ENV PYTHONUNBUFFERED 1

EXPOSE 9090

CMD python3.8 ./jeu_devinette_obstacles.py