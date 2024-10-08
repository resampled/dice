from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('postlist/', views.PostListView.as_view(), name='post-list'),
    path('userlist/', views.UserListView.as_view(), name='user-list'),
    path('accounts/profile/', views.UserProfile, name='user-profile'),
    path('new/', views.PostCreate.as_view(), name='post-create'),
    path('post/<slug:author>/<slug:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<slug:author>/<slug:pk>/edit', views.PostUpdate.as_view(), name='post-update'),
    path('post/<slug:author>/<slug:pk>/delete', views.PostDelete.as_view(), name='post-delete'),
    path('user/<slug:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('user/<slug:pk>/edit', views.UserUpdate.as_view(), name='user-update'),
    path('comment/<slug:pk>/delete', views.CommentDelete.as_view(), name='comment-delete'),
]
