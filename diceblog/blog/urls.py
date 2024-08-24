from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('postlist/', views.PostListView.as_view(), name='post-list'),
    path('post/<slug:pk>', views.PostDetailView.as_view(), name='post-detail'),
]
