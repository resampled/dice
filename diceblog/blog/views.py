import datetime
from django.shortcuts import render
from django.views import generic
from .models import BlogPost, BlogUser, BlogComment
from django.contrib.auth.mixins import LoginRequiredMixin
# from .models import -MODELS-

def homepage(request):
    context = {
        'datetime': datetime.datetime.now,
    }
    return render(request, 'homepage.html', context=context)

class PostListView(generic.ListView):
    model = BlogPost
    paginate_by = 10

class PostDetailView(generic.DetailView):
    model = BlogPost

def UserProfile(request):
    context = {
    }
    return render(request, 'user_profile.html', context=context)
