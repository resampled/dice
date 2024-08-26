from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
import datetime
from nanoid import generate

class BlogUser(AbstractUser):
    username = models.SlugField(max_length=20, unique=True)
    description = models.TextField(max_length=500)
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.username

def make_order():
    return float(datetime.datetime.now().timestamp())
def make_id(chars):
    return str(generate('1234567890bcdfghijkmnpqrstuvwxyz', chars))

class BlogPost(models.Model):
    title = models.CharField(max_length=240, unique=True)
    order = models.FloatField(default=make_order)
    id = models.SlugField(unique=True,primary_key=True,default=make_id(8))
    # preformatted content
    pre_content = models.TextField(max_length=80000)
    author = models.ForeignKey('BlogUser',on_delete=models.RESTRICT, null=True)
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.id,'author':self.author.username})
    def __str__(self):
        return self.title

class BlogComment(models.Model):
    assigned_post = models.ForeignKey('BlogPost',on_delete=models.RESTRICT, null=True)
    author = models.ForeignKey('BlogUser',on_delete=models.RESTRICT, null=True)
    content = models.TextField(max_length=1700)
    order = models.FloatField(default=make_order)
    id = models.SlugField(unique=True,primary_key=True,default=make_id(8))
    def __str__(self):
        return self.content[:90]
