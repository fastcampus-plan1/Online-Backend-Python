from django.contrib import admin
from django.contrib import messages

from .models import Product
from .admin_helper import log_change

@admin.action(description="선택한 상품을 판매중으로 변경하기")
def make_on_sale(modeladmin, request, queryset):
    changed_objs = list(queryset.filter(on_sale=False))
    queryset.update(on_sale=True)
    messages.info(request, f"{len(changed_objs)}개의 상품을 판매중으로 변경했습니다.")
    for obj in changed_objs:
        log_change(request.user, obj, "on_sale=True로 변경되었습니다.")

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "created_at", "updated_at"]
    fields = ["name", "price", "description", "tags", "on_sale"]
    search_fields = ["name"]
    actions = [make_on_sale]