release: python manage.py migrate
web: gunicorn TreesUni.wsgi:application --log-file -
python manage.py collectstatic --noinput
