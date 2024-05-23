from django.contrib import admin

from restaurant.models import Restaurant


class RestaurantAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "category",
        "phone",
        "rating",
        "rating_count",
        "created_at",
        "updated_at",
    ]
    search_fields = ["name", "phone"]


admin.site.register(Restaurant, RestaurantAdmin)
