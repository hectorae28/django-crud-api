#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
python manage.py createsuperuser --username USERNAME --email EMAIL --password DJANGO_SUPERUSER_PASSWORD --no-input