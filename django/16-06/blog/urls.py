from django.urls import path

from .views import post_list, post_create, post_edit

app_name = 'blog'

urlpatterns = [
    path('posts', post_list, name='post_list'),
    path('posts/create/', post_create, name='post_create'),
    path('posts/<int:pk>/', post_edit, name='post_edit'),
]