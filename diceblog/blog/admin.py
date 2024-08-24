from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import BlogUser, BlogPost, BlogComment

# Register your models here.

admin.site.register(BlogUser)
admin.site.register(BlogPost)
admin.site.register(BlogComment)

