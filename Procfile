web: cd diceblog && python manage.py migrate && python createsuperuser --no-input --username=admin && python manage.py collectstatic --no-input && gunicorn dice.wsgi:application
