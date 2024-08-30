import datetime
from django.shortcuts import render
from django.views import generic
from .models import BlogPost, BlogUser, BlogComment
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect

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
                # https://blog.extrovert.dev/2021/05/get-current-logged-in-user-in-django.html
                cmt = BlogComment.create(
                    assigned_post=self.get_object(),
                    author=self.request.user,
                    content=request.POST["content"]
                )
                cmt.save()
                # TODO push this to DB
                # and make a proper redirect to the GET page                
                return HttpResponseRedirect("")
@login_required
def UserProfile(request):
    context = {
    }
    return render(request, 'user_profile.html', context=context)


