import datetime
from django.shortcuts import render
from django.views import generic
from .models import BlogPost, BlogUser, BlogComment
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


