import re
import datetime
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import BlogPost, BlogUser, BlogComment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from nanoid import generate

user = get_user_model()

#imported from models.py
def make_order():
    return datetime.datetime.now()
def make_id(chars):
    return str(generate('1234567890bcdfghijkmnpqrstuvwxyz', chars))

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
                    content=request.POST["content"],
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

class PostCreate(LoginRequiredMixin, CreateView):
    model = BlogPost
    fields = ['title', 'pre_content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.id = make_id(8) # stop id freezing bug
        return super().form_valid(form)

class PostUpdate(LoginRequiredMixin, UpdateView):
    # this is a bit scuffed
    model = BlogPost
    fields = ['title', 'pre_content']
    def get(self, request, *args, **kwargs):
        # check if editor is author, or if editor is admin
        if request.user.username == kwargs["author"] or request.user.has_perm('change_blogpost'):
            # get context to generate form...probably not efficient
            kwargs['formtype'] = 'update'
            postpk = kwargs["pk"]
            postobj = BlogPost.objects.get(id=f'{postpk}')
            kwargs['title'] = postobj.title
            kwargs['content'] = postobj.pre_content
            return render(request,'blog/blogpost_form.html',kwargs)
        else:
            return HttpResponse("fail")

class PostDelete(LoginRequiredMixin, DeleteView):
    model = BlogPost
    success_url = reverse_lazy('post-list') #change this
    def get(self, request, *args, **kwargs):
        # check if editor is author, or if editor is admin
        if request.user.username == kwargs["author"] or request.user.has_perm('delete_blogpost'):
            kwargs['formtype'] = 'delete'
            return render(request,'blog/blogpost_form.html',kwargs)
        else:
            return HttpResponse("fail")

