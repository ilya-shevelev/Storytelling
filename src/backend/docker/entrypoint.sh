#!/bin/bash

set -euo pipefail

python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
if [[ "$DJANGO_ENV" = "prod" ]]; then
  gunicorn --bind 0.0.0.0:8000 config.wsgi:application
else
  python manage.py runserver 0.0.0.0:8000
fi
