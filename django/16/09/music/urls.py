from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'music'

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name="index"),
    path('artists/', views.artist_list, name="artist_list"),
    path('artists/<int:id>/', views.artist_detail, name="artist_detail"),
    path('albums/', views.albums_list, name="album_list"),
    path('albums/<int:id>/', views.albums_detail, name="album_detail"),
    path('statistics/', views.statistics_view, name="statistics"),
]