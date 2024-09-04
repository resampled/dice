from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
import datetime
from nanoid import generate

blog_title_max = 240
blog_content_max = 80000
comment_max = 1700

class BlogUser(AbstractUser):
    username = models.SlugField(max_length=20, unique=True)
    description = models.TextField(max_length=500)
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.username
    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])

def make_order():
    return datetime.datetime.now()
def make_id(chars):
    return str(generate('1234567890bcdfghijkmnpqrstuvwxyz', chars))

class BlogPost(models.Model):
    title = models.CharField(max_length=blog_title_max, unique=True, help_text=f"max: {blog_title_max}")
    order = models.DateTimeField(default=make_order)
    id = models.SlugField(unique=True,primary_key=True,default=make_id(8))
    # preformatted content
    pre_content = models.TextField(max_length=blog_content_max,verbose_name="Body",help_text=f"max: {blog_content_max}")
    author = models.ForeignKey('BlogUser',on_delete=models.RESTRICT, null=True)
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.id,'author':self.author.username})
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-order']

class BlogComment(models.Model):
    assigned_post = models.ForeignKey('BlogPost',on_delete=models.RESTRICT, null=True)
    author = models.ForeignKey('BlogUser',on_delete=models.RESTRICT, null=True)
    # let's try out this one soon...    
    #parent = models.ForeignKey('BlogComment',on_delete=models.CASCADE, null=True)
    content = models.TextField(max_length=comment_max)
    order = models.DateTimeField(default=make_order)
    id = models.SlugField(unique=True,primary_key=True,default=make_id(18))
    def create(assigned_post,author,content):
        return BlogComment(assigned_post=assigned_post,author=author,content=content,order=make_order(),id=make_id(8))
    def __str__(self):
        return self.content[:90]    
    class Meta:
        ordering = ['order']
