from django.contrib import admin
from django.db.models import Count

from .models import Restaurants, RestaurantBlogReviews


class RestaurantBlogReviewsInline(admin.TabularInline):
    model = RestaurantBlogReviews
    extra = 0  # 추가 폼을 보여주지 않음
    fields = ['title', 'published_date', 'blog_url']  # 보여줄 필드
    readonly_fields = ['title', 'published_date', 'blog_url']
    can_delete = False  # 삭제 옵션 비활성화
    show_change_link = True  # 변경 링크 활성화


class RestaurantAdmin(admin.ModelAdmin):
    # 리스트 뷰 커스터마이징
    list_display = ('name', 'cuisine_type', 'category', 'rating', 'rating_count', "blog_reviews_count")
    list_filter = ('cuisine_type', 'category', )
    search_fields = ('name', 'tags', 'keyword', 'address')

    def get_queryset(self, request):
        # annotate를 사용하여 각 레스토랑에 대한 블로그 리뷰의 수를 계산
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _blog_reviews_count=Count('restaurantblogreviews')
        )
        return queryset

    def blog_reviews_count(self, obj):
        # Annotated 값 사용
        return obj._blog_reviews_count
    
    blog_reviews_count.admin_order_field = '_blog_reviews_count'
    blog_reviews_count.short_description = 'Blog Reviews Count'
    

    # 디테일 뷰 커스터마이징
    inlines = [RestaurantBlogReviewsInline]

    fieldsets = (
        (None, {
            'fields': ('name', 'area_name', 'kakao_place_id', 'address', 'phone')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('cuisine_type', 'category', 'tags', 'menu', 'rating', 'keyword', 'rating_count', 'business_hour', 'latitude', 'longitude')
        }),
    )
    readonly_fields = ('created_at', 'updated_at')


class RestaurantBlogReviewAdmin(admin.ModelAdmin):
    list_display = ("title", "blog_url", "published_date", "restaurant_name")

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related("restaurant")
        return queryset

    def restaurant_name(self, obj):
        return obj.restaurant.name
    
    restaurant_name.admin_order_field = "restaurant__name"

admin.site.register(Restaurants, RestaurantAdmin)
admin.site.register(RestaurantBlogReviews, RestaurantBlogReviewAdmin)
