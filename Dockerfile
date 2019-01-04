FROM python:3.6

EXPOSE 8000
WORKDIR /app
ENTRYPOINT ["./docker-entrypoint.sh"]

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /app/requirements.txt
COPY ./docker-entrypoint.sh /app/docker-entrypoint.sh
RUN pip install -r requirements.txt
COPY ./base /app/
