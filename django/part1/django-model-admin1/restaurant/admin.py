from django.contrib import admin

from restaurant.models import (
    Restaurant,
    RestaurantCategory,
    RestaurantStatistics,
    Keyword,
)


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
    list_filter = ["category", "rating"]


admin.site.register(Restaurant, RestaurantAdmin)


admin.site.register(RestaurantCategory)


admin.site.register(RestaurantStatistics)


class KeywordAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ["id", "name"]
    search_fields = ["name"]


admin.site.register(Keyword, KeywordAdmin)
