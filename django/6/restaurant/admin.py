from django.contrib import admin

from restaurant.models import Restaurant

# 기본 어드민을 사용할 때 모델만 등록
#admin.site.register(Restaurant)

class RestaurantAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "phone",
        "rating",
        "created_at",
        "updated_at",
    ]
    fields = ["name", "phone", "rating"]

# 모델 어드민 클래스를 등록할 때는 모델과 모델 어드민 클래스를 함께 등록
admin.site.register(Restaurant, RestaurantAdmin)
