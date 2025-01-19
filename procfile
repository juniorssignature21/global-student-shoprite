web: gunicorn ecom_proj.wsgi --log-file -

web: gunicorn ecom_proj.wsgi:application --bind 0.0.0.0:$PORT

web: python manage.py migrate