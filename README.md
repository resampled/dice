**Dice** (aka Diceblog) is a Django-powered lightweight blogging platform as following [Mozilla's Django assessment](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/django_assessment_blog).

Be warned that currently this software is in active development and not fully implemented. Please do not attempt to deploy or use this software yourself at this point in time, or you will be really disappointed.

Read `todo.txt` for a list of features currently planned or in development.
# Requirements
Python 3.12.3 is used for development. Realistically, this app should work on any Python version supported by the latest versions of Django and the other packages.

So far, the following Python packages are required (additional packages may be listed in the future):
* Django (`pip install Django==5.1`)
* nanoid (`pip install nanoid==2.0.0`)
* django-allauth (`pip install django-allauth==64.1.0`)

You can also retrieve these packages via requirements.txt.

# Installation
This section will be filled out more comprehensively once Dice is safe for usage.

Nevertheless, if you already know how to setup a Django project, you won't have to deal with many shenanigans - just cd into the project, install dependencies, makemigrations, migrate, and runserver.
