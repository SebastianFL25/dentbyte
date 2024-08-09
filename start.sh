#!/bin/bash 

docker build --no-cache -t

python manage.py makemigrations --no-input
python manage.py migrate --no-input

python manage.py runserver 0.0.0.0:8000