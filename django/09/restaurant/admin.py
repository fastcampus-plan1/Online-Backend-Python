from django.contrib import admin

from restaurant.models import Restaurant, RestaurantCategory, RestaurantStatistics, Keyword

def reset_rating(modeladmin, request, queryset):
    queryset.update(rating=0.0, rating_count=0)
reset_rating.short_description = "선택된 가게의 별점 초기화"


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'phone', 'rating', 'rating_count', 'created_at', 'updated_at']
    list_display_links = ['id', 'name']
    list_filter = ['category', 'rating']
    search_fields = ['name', 'phone']
    ordering = ['-id']
    actions = [reset_rating]
    autocomplete_fields = ['keywords']

    
admin.site.register(Restaurant, RestaurantAdmin)


admin.site.register(RestaurantCategory)


admin.site.register(RestaurantStatistics)


class KeywordAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']
admin.site.register(Keyword, KeywordAdmin)