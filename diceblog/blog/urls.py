from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('postlist/', views.PostListView.as_view(), name='post-list'),
    path('userlist/', views.UserListView.as_view(), name='user-list'),
    path('accounts/profile/', views.UserProfile, name='user-profile'),
    path('post/<slug:author>/<slug:pk>', views.PostDetailView.as_view(), name='post-detail'),
]
