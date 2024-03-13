from django.contrib import admin
from django.urls import path, reverse
from django.shortcuts import render
from django.utils.safestring import mark_safe

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "created_at", "updated_at", "view_image_link"]
    fields = ["name", "price", "description", "image", "tags"]
    search_fields = ["name"]

    change_form_template = "admin/product/change_form.html"

    def view_image_link(self, obj):
        link = reverse("admin:product_view_image", args=[obj.id])
        return mark_safe(f'<a href="{link}">이미지 보기</a>') if obj.image else ""

    def get_urls(self):
        urls = super().get_urls()
        urls = [
            path("<path:object_id>/view-image/", self.view_image, name="product_view_image"),
        ] + urls
        return urls
    
    def view_image(self, request, object_id):
        self.has_view_or_change_permission(request)
        product = Product.objects.get(id=object_id)
        image = product.image
        title = product.name
        return render(request, "admin/product/view_image.html", {
            "opts": self.model._meta,
            "original": product,
            "has_permission": True,
            "title": title,
            "image": image,
        })
