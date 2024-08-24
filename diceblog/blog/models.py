from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
import datetime
from nanoid import generate # NanoID package required from pip, I use 2.0.0

class BlogUser(AbstractUser):
    username = models.SlugField(max_length=20, unique=True)
    description = models.TextField(max_length=500)
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.username

class BlogPost(models.Model):
    title = models.CharField(max_length=240, unique=True)
    order = models.FloatField()
    id = models.SlugField(unique=True,primary_key=True)
    # preformatted content
    pre_content = models.TextField(max_length=20000)
    author = models.ForeignKey('BlogUser',on_delete=models.RESTRICT, null=True)
    def CreateID(self):
        order = datetime.datetime.now().timestamp()
        id = generate('1234567890bcdfghijkmnpqrstuvwxyz', 8)
        pass
    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])
    def __str__(self):
        return self.title

class BlogComment(models.Model):
    assigned_post = models.ForeignKey('BlogPost',on_delete=models.RESTRICT, null=True)
    author = models.ForeignKey('BlogUser',on_delete=models.RESTRICT, null=True)
    content = models.TextField(max_length=1700)
    def __str__(self):
        return self.id
