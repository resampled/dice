web: cd diceblog && python manage.py migrate && python manage.py collectstatic --no-input && python manage.py syncdb && gunicorn dice.wsgi:application
