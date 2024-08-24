from django.db import models
from django.contrib.auth.models import AbstractUser

class BlogUser(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    description = models.TextField(max_length=500)
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.username

# todo make these

class BlogPost(models.Model):
    pass

class BlogComment(models.Model):
    pass


