from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('v1/albums/', views.albums_list, name="albums_list"),
]