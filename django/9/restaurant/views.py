def index_view(request):
    return render(request, 'index.html')


def restaurant_view(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    return render(request, 'restaurant.html', {'restaurant': restaurant})
