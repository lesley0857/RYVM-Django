#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn Ryvm_project.wsgi:app --bind 0.0.0.0:8000
