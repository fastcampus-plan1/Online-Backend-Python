from rest_framework import viewsets

from restaurant.models import Restaurant
from .serializers import RestaurantSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
