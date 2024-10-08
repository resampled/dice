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
from django.shortcuts import render, get_object_or_404
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

def detect_whitespace_only(s):
    if s == "" or re.match(r"^\s+$", s):
        return True
    return False

class PostDetailView(generic.DetailView):
    model = BlogPost
    # cmtbox (for guests this isn't used - shows a non-functional mimic form instead)
    def post(self, request, *args, **kwargs):
            if user.is_authenticated:
                if 'cmtsubmit' in request.POST:
                    # make comment model and save it. not the easiest way to do this
                    cmt = BlogComment.create(
                        assigned_post=self.get_object(),
                        author=self.request.user,
                        content=request.POST["content"],
                    )
                    if detect_whitespace_only(cmt.content):
                        return HttpResponseRedirect("")
                    # approve
                    cmt.save()             
                    return HttpResponseRedirect("")
                elif 'replysubmit' in request.POST:
                    cmt = BlogComment.create_reply(
                        assigned_post=self.get_object(),
                        author=self.request.user,
                        content=request.POST["content"],
                        parent=get_object_or_404(BlogComment,pk=request.POST.get('parent',0)),
                    )
                    if detect_whitespace_only(cmt.content):
                        return HttpResponseRedirect("")
                    cmt.save()
                    return HttpResponseRedirect("")
                else:
                    return HttpResponse("fail! (bad POST)")
            else:
                return HttpResponse("fail! (form submit while logged out)")

class UserDetailView(generic.DetailView):
    model = BlogUser
    paginate_by = 10

@login_required
def UserProfile(request):
    context = {
    }
    return render(request, 'user_profile.html', context=context)

# update user profile (/user/000)
class UserUpdate(LoginRequiredMixin, UpdateView):
    model = BlogUser
    fields = ['description']

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
    success_url = reverse_lazy('post-list') #replace?
    # todo: rework this to CommentDelete's implementation
    # and make it its own template instead of sharing with PostUpdate.
    # yes my code is SHIT but hey thats why i'm doing this    
    def get(self, request, *args, **kwargs):
        # check if editor is author, or if editor is admin
        if request.user.username == kwargs["author"] or request.user.has_perm('delete_blogpost'):
            kwargs['formtype'] = 'delete'
            return render(request,'blog/blogpost_form.html',kwargs)
        else:
            return HttpResponse("fail")

class CommentDelete(LoginRequiredMixin, DeleteView):
    model = BlogComment
    success_url = reverse_lazy('post-list') #replace?
    # check if editor is author, or if editor is admin    
    def get_queryset(self):
        queryset = super(CommentDelete, self).get_queryset()
        if self.request.user.has_perm('delete_blogcomment'):
            return queryset.filter() 
        return queryset.filter(author=self.request.user)

"""    def get(self, request, *args, **kwargs):
        cmtpk = kwargs["pk"]
        cmtobj = BlogComment.objects.get(id=f'{cmtpk}')
        # check if editor is author, or if editor is admin
        if request.user.username == cmtobj.author or request.user.has_perm('delete_blogcomment'):
            return render(request,'blog/blogcomment_confirm_delete.html',kwargs)
        else:
            return HttpResponse("fail")
"""
