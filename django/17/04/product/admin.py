from django.contrib import admin
from rangefilter.filters import DateRangeFilter

from .models import Product, ProductOption, Tag

 
class ProductOptionInline(admin.StackedInline):
    model = ProductOption   
    extra = 1


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]


class PriceFilter(admin.SimpleListFilter):
    title = "가격"
    parameter_name = "price"

    def lookups(self, request, model_admin):
        return [
            ("10000", "1만원 이하"),
            ("50000", "1~5만원"),
            ("100000", "5~10만원"),
            ("999999", "10만원 이상"),
        ]

    def queryset(self, request, queryset):
        if self.value() == "10000":
            return queryset.filter(price__lte=10_000)
        if self.value() == "50000":
            return queryset.filter(price__range=[10_000, 50_000])
        if self.value() == "100000":
            return queryset.filter(price__range=[50_000, 100_000])
        if self.value() == "999999":
            return queryset.filter(price__gte=100_000)
        


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    목록 뷰 설정
    """
    list_display = ["id", "name", "price", "created_at", "updated_at"]
    # 검색 필드
    search_fields = ["name"]

    # 정렬 순서
    ordering = ["created_at"]

    list_filter = [
        PriceFilter,
        #("created_at", admin.DateFieldListFilter),
        #("updated_at", admin.DateFieldListFilter),
        #("on_sale", admin.BooleanFieldListFilter),
        #("tags", admin.RelatedOnlyFieldListFilter),
        #("description", admin.EmptyFieldListFilter),
        ("created_at", DateRangeFilter),
        ("updated_at", DateRangeFilter),
    ]


    """
    상세 정보 / 편집 뷰 설정
    """
    fieldsets = (
        (None, {
            "fields": (
                "name",
                "price",
            ),
        }),
        ("선택 정보", {
            "fields": (
                "description",
                "tags",
            ),
            "classes": ("collapse",),
        }),
    )
    
    # 인라인
    inlines = [ProductOptionInline]

