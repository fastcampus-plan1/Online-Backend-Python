from django.contrib import admin

from .models import Product, StaffProduct


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "created_at", "updated_at"]
    fields = ["name", "price", "description", "tags",  "staffs"]
    search_fields = ["name"]


@admin.register(StaffProduct)
class StaffProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "created_at", "updated_at"]
    fields = ["name", "description", "tags"]
    search_fields = ["name"]

    def get_queryset(self, request):
        if request.user.is_superuser:
            return super().get_queryset(request)
        return super().get_queryset(request).filter(staffs=request.user)

    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, reqeust, obj=None):
        return False
    
