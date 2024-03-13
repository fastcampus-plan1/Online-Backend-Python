from django.contrib import admin, messages

from .actions import export_as_csv
from .models import Product


admin.site.add_action(export_as_csv)
admin.site.disable_action("delete_selected")

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "created_at", "updated_at"]
    fields = ["name", "price", "description", "tags"]
    search_fields = ["name"]
    actions = ["make_not_on_sale", "delete_selected"]

    @admin.action(description="선택된 상품을 비활성화합니다")
    def make_not_on_sale(modeladmin, request, queryset):
        queryset.update(on_sale=False)
        messages.info(request, f"{queryset.count()}개의 항목을 비활성화했습니다.")
