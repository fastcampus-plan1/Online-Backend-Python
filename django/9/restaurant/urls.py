from django.urls import path

from .views import index_view, restaurant_view

urlpatterns = [
    path('', index_view, name='index'),
    path('restaurant/<int:restaurant_id>', restaurant_view, name='restaurant'),
]
