from django.contrib import admin

# Register your models here.

from .models import (
    Article,
    CuisineType,
    RestaurantCategory,
    Restaurant,
    Keyword,
    RestaurantImage,
    RestaurantMenu,
    Review,
    SocialChannel,
    Tag,
)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "preview_content", "created_at", "updated_at"]
    search_fields = ["title"]


@admin.register(CuisineType)
class CuisineTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(RestaurantCategory)
class RestaurantCategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.action(description="별점을 1로 변경")
def set_rating_to_1(modeladmin, request, queryset):
    queryset.update(rating=1)


class RestaurantImageInline(admin.TabularInline):
    model = RestaurantImage
    extra = 1


class RestaurantMenuInline(admin.TabularInline):
    model = RestaurantMenu
    extra = 1


class HasImageFilter(admin.SimpleListFilter):
    title = "이미지 있음"
    parameter_name = "has_image"

    def lookups(self, request, model_admin):
        return (("yes", "Yes"), ("no", "No"))

    def queryset(self, request, queryset):
        if self.value() == "yes":
            return queryset.exclude(image="")
        if self.value() == "no":
            return queryset.filter(image="")


class RatingFilter(admin.SimpleListFilter):
    title = "별점"
    parameter_name = "rating"

    def lookups(self, request, model_admin):
        return (("1~2", "1~2"), ("2~3", "2~3"), ("3~4", "3~4"), ("4~5", "4~5"))

    def queryset(self, request, queryset):
        if self.value() == "0~1":
            return queryset.filter(rating__lte=1, rating__gte=0)
        if self.value() == "1~2":
            return queryset.filter(rating__lte=2, rating__gte=1)
        if self.value() == "2~3":
            return queryset.filter(rating__lte=3, rating__gte=2)
        if self.value() == "3~4":
            return queryset.filter(rating__lte=4, rating__gte=3)
        if self.value() == "4~5":
            return queryset.filter(rating__lte=5, rating__gte=4)


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ["name", "address", "phone", "rating", "has_image"]
    list_filter = [RatingFilter, HasImageFilter]
    inlines = [RestaurantImageInline, RestaurantMenuInline]
    search_fields = ["name"]
    actions = [set_rating_to_1]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "created_at", "updated_at"]
    search_fields = ["title"]


@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(RestaurantMenu)
class RestaurantMenuAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "created_at", "updated_at"]
    search_fields = ["name"]


@admin.register(SocialChannel)
class SocialChannelAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
