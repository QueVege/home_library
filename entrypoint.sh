#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done
fi

python manage.py flush --no-input
python manage.py collectstatic --no-input --clear
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000

exec "$@"