from django.urls import include, path

from rest_framework import routers

from .views import RestaurantViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register(r"restaurants", RestaurantViewSet, basename="restaurants")

urlpatterns = [
    path("", include(router.urls)),
]
