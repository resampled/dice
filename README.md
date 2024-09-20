**Dice** (aka Diceblog) is a Django-powered lightweight blogging platform as following [Mozilla's Django assessment](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/django_assessment_blog).

Be warned that currently this software is in active development and not fully implemented. Beware of disappointment.

Read `todo.txt` for a list of features currently planned or in development.
# Requirements
Python 3.12.3 is used for development. Realistically, this app should work on any Python version supported by the latest versions of Django and the other packages.

# Installation
1. Clone or download this project (use `main` branch for testing, `deploy` for production)
2. Get pip to install the dependencies listed in `requirements.txt`.
3. Configure `/dice/settings.py` to your liking. 
* FOR TESTING:
1. `python manage.py migrate` and `python manage.py runserver`.
* FOR DEPLOYMENT:
1. Connect to a Postgres database and fill out the environment variables left in `/dice/settings.py` - or change it to your own DB (may cause issues).
2. Copy the command in `Procfile` and paste, leaving out the `web: ` at the start (if you use Railway or another service that uses the Procfile, this is done automatically)
