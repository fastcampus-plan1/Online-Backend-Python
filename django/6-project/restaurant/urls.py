from django.urls import path

from .views import index

app_name = "restaurant"

urlpatterns = [
    path("", index, name="index"),
]
