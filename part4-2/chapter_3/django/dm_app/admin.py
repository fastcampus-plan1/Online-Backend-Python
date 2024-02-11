from django.contrib import admin
from django.db.models import Count
from django.http.request import HttpRequest
from django.template.response import TemplateResponse

import pandas as pd
import plotly.express as px
from plotly.offline import plot
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import base64
from io import BytesIO


from .models import Restaurants, RestaurantBlogReviews


class RestaurantBlogReviewsInline(admin.TabularInline):
    model = RestaurantBlogReviews
    extra = 0  # 추가 폼을 보여주지 않음
    fields = ['title', 'published_date', 'blog_url']  # 보여줄 필드
    readonly_fields = ['title', 'published_date', 'blog_url']
    can_delete = False  # 삭제 옵션 비활성화
    show_change_link = True  # 변경 링크 활성화


class RestaurantAdmin(admin.ModelAdmin):
    change_list_template = "restaurant_change_list.html"

    def create_plotly_chart(self):
       # 예시 데이터로 그래프 생성
       qs = Restaurants.objects.values('category').annotate(count=Count('id'))
       df = pd.DataFrame(list(qs))
       fig = px.bar(
           df, 
           x='category', 
           y='count', 
           color="category",
           labels={'count':'Number of Restaurants', 'category': 'Category'},
           width=1200,
           height=500,
       )

       # Plotly 그래프를 HTML 문자열로 변환
       graph_html = plot(fig, output_type='div', include_plotlyjs=True)
       return graph_html
    
    def create_mpl_chart(self):
       qs = Restaurants.objects.values('category').annotate(count=Count('id'))
       df = pd.DataFrame(list(qs))

       plt.figure()
       plt.bar(df['category'], df['count'])
       plt.ylabel("counts")
       plt.xlabel("category")
       plt.title("restaurant counts")

       buf = BytesIO()
       plt.savefig(buf, format="png")
       buf.seek(0)

       img_base64 = base64.b64encode(buf.getvalue()).decode("utf-8")
       buf.close()
       return img_base64

    def changelist_view(self, request, extra_context=None):
       # 그래프 HTML 생성
       graph_html = self.create_plotly_chart()
       mpl_img = self.create_mpl_chart()
       extra_context = extra_context or {}
       extra_context['graph_html'] = graph_html
       extra_context['mpl_img'] = mpl_img

       return super().changelist_view(request, extra_context=extra_context)


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

    def custom_action(self, request, queryset):
        for obj in queryset:
            # 테이블하나 생성하세요. 
            # id와 카카오 플레이스 id를 해당 테이블에 삽입
            # 이미 수집중인 리뷰가 있다면, 해당 내용은 수집등록하지 않습니다.

            print(obj.id, obj.kakao_place_id)
        self.message_user(request, "리뷰 수집이 성공적으로 등록되었습니다.")
    custom_action.short_description = "리뷰 수집하기"
    actions = [custom_action]

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
