from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    #UserPostListView    
)

urlpatterns = [
    #path('', PostListView.as_view(), name='blog-home'),
    path('', PostCreateView.as_view(), name='blog-home'),
    path('list/', PostListView.as_view(), name='blog-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('chart/', views.chart, name='blog-chart'),
    path('about/', views.about, name='blog-about'),
    # path('name/', views.name, name='blog-name'),
]
