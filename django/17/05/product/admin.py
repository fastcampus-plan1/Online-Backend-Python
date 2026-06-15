from django.contrib import admin

from .models import Product

admin.site.site_header = "쇼핑몰 관리자"
admin.site.site_title = "쇼핑몰 관리자"
admin.site.index_title = ""
admin.site.enable_nav_sidebar = False
admin.site.empty_value_display = "(비어있음)"

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "created_at", "updated_at"]
    fields = ["name", "price", "description", "tags"]
    search_fields = ["name"]
