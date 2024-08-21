from django.db import models
from django.contrib.auth.models import AbstractUser

class BlogUser(AbstractUser)
    username = models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    email = models.EmailField()
    def __str__(self):
        return self.username

# todo: implement abstract user model
