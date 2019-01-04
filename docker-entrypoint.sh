#!/bin/bash
python manage.py collectstatic --noinput  # collect static files
python manage.py migrate --noinput  # migrate database

exec gunicorn --bind 0.0.0.0:8000 base.wsgi
