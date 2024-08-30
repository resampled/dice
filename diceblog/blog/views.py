import datetime
from django.shortcuts import render
from django.views import generic
from .models import BlogPost, BlogUser, BlogComment
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

user = get_user_model()

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
    # cmtbox (login should be enforced at template)
    def post(self, request, *args, **kwargs):
            if user.is_authenticated and 'cmtsubmit' in request.POST and 'content' in request.POST:
                #BlogComment.create(assigned_post=self.get_object(),author=request.user,content="content")
                # TODO  make "author=" go to the current user
@login_required
def UserProfile(request):
    context = {
    }
    return render(request, 'user_profile.html', context=context)


