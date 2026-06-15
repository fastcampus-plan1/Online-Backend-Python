from django.contrib import admin

from restaurant.models import Restaurant


class RestaurantAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "phone",
        "rating",
        "created_at",
        "updated_at",
    ]
    search_fields = ["name", "phone"]


admin.site.register(Restaurant, RestaurantAdmin)
