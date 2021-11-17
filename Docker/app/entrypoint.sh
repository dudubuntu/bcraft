#!/bin/bash

python manage.py makemigrations --no-input

python manage.py makemigrations web --no-input

python manage.py migrate --no-input

python manage.py migrate web --no-input

python manage.py createsuperuser --no-input

if [ $COLLECT_STATIC ]
    then
        python manage.py collectstatic --no-input
fi

exec gunicorn bcraft_app.wsgi:application -b 0.0.0.0:8000 --reload