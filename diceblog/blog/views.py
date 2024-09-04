import re
import datetime
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import BlogPost, BlogUser, BlogComment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
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

class UserListView(generic.ListView):
    model = BlogUser
    paginate_by = 10

class PostDetailView(generic.DetailView):
    model = BlogPost
    # cmtbox (for guests this isn't used - shows a non-functional mimic form instead)
    def post(self, request, *args, **kwargs):
            if user.is_authenticated and 'cmtsubmit' in request.POST and 'content' in request.POST:
                # make comment model and save it. not the easiest way to do this
                cmt = BlogComment.create(
                    assigned_post=self.get_object(),
                    author=self.request.user,
                    content=request.POST["content"]
                )
                # detect whitespace only comment
                if cmt.content == "" or re.match(r"^\s+$", cmt.content):
                    return HttpResponseRedirect("")
                # approve
                cmt.save()             
                return HttpResponseRedirect("")

class UserDetailView(generic.DetailView):
    model = BlogUser
    paginate_by = 10

@login_required
def UserProfile(request):
    context = {
    }
    return render(request, 'user_profile.html', context=context)

class PostCreate(PermissionRequiredMixin, CreateView):
    model = BlogPost
    fields = ['title', 'pre_content']
    permission_required = 'catalog.add_blogpost'

class PostUpdate(PermissionRequiredMixin, UpdateView):
    model = BlogPost
    fields = ['title', 'pre_content']
    permission_required = 'catalog.change_blogpost'

class PostDelete(PermissionRequiredMixin, DeleteView):
    model = BlogPost
    success_url = reverse_lazy('post-list') #change this
    permission_required = 'catalog.delete_blogpost'
