from django.contrib import admin
from django.http import HttpRequest

from .models import Product, ProductOption


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "created_at", "updated_at"]
    fields = ["name", "price", "description", "tags"]
    search_fields = ["name"]

    filter_horizontal = ["tags"]


@admin.register(ProductOption)
class ProductOptionAdmin(admin.ModelAdmin):
    list_display = ["id", "product", "color", "size", "stock"]
    list_filter = ["color", "size"]
    search_fields = ["product__name"]
    list_select_related = ["product"]

    def has_add_permission(self, request: HttpRequest) -> bool:
        # return super().has_add_permission(request)
        return False

    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        # return super().has_change_permission(request, obj)
        return False

    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        # return super().has_delete_permission(request, obj)
        return False

    def has_view_permission(self, request: HttpRequest, obj=None) -> bool:
        # 이 메소드는 False를 반환하면 어드민에서 해당 객체를 볼 수 없습니다.
        return super().has_view_permission(request, obj)
