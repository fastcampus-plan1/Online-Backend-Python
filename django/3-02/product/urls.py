from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.urls import path

from .views import view1, view2, View3, increase_sotck, decrease_stock

app_name = "product"

urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html")),
    path(
        "login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("view1/", view1, name="view1"),
    path("view2/", view2, name="view2"),
    path("view3/", View3.as_view(), name="view3"),
    path("increase_stock/", increase_sotck, name="increase_stock"),
    path("decrease_stock/", decrease_stock, name="decrease_stock"),
]
