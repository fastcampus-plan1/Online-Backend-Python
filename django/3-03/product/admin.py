from django.contrib import admin

from .models import Product, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    목록 뷰 설정
    """
    list_display = ["id", "name", "price", "created_at", "updated_at"]
    # 검색 필드
    search_fields = ["name"]
    search_help_text = "상품 이름을 입력해주세요."
    readonly_fields = ["name_and_price"]

    # 정렬 순서
    ordering = ["created_at"]

    # 링크될 필드
    #list_display_links = ["id", "name"]

    # 페이지당 보여질 아이템 수
    #list_per_page = 2

    # 필드 오버라이딩
    #formfield_overrides = {
    #    models.CharField: {"widget": TextInput(attrs={"size": "100"})},
    #}

    # 편집 가능한 필드
    #list_editable = ["price"]

    """
    상세 정보 / 편집 뷰 설정
    """
    fields = [("name", "price"), "name_and_price", "description"]
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
    """
    
    # 읽기만 가능하도록
    #readonly_fields = ["name", "price", "description"]

    # 빈 값 표시
    empty_value_display = "-비어있음-"

    # 세가지 중 하나만 사용 가능
    #filter_horizontal = ["tags"]
    #filter_vertical = ["tags"]
    #raw_id_fields = ["tags"]
    autocomplete_fields = ["tags"]

    #save_as = True
    #save_as_continue = True
    #save_on_top = True

    @admin.display(description="상품명 / 가격")
    def name_and_price(self, obj):
        return f"{obj.name} / {obj.price}"
