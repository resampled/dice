from blog.models import BlogUser
user = BlogUser.objects.get(username='admin', is_superuser=True)
user.delete()
