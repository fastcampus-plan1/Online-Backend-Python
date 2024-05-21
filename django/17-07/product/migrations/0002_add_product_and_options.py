from django.db import migrations
from product.models import Product, ProductOption, Tag


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0001_initial"),
    ]

    def add_mens_clothes(apps, schema_editor):
        # Create products
        product1 = Product.objects.create(
            name="엘리건트 데님",
            price=50000,
            description="우아하고 세련된 실루엣을 제공하는 엘리건트 데님입니다. \n프리미엄 코튼 혼방 소재로 제작되어 편안함과 내구성을 동시에 제공합니다.\n매일의 스타일을 높여줄 완벽한 선택입니다.",
        )
        product2 = Product.objects.create(
            name="클래식 슬랙스",
            price=70000,
            description="고급스러운 소재와 클래식한 디자인이 조화를 이루는 슬랙스입니다.\n부드러운 울 혼방 소재로 제작되어, 비즈니스 미팅부터 캐주얼한 모임까지,\n다양한 상황에 어울립니다.",
        )
        product3 = Product.objects.create(
            name="럭셔리 가죽 자켓",
            price=150000,
            description="최고급 가죽으로 제작된 럭셔리 자켓으로, 시간이 지날수록 더욱 멋스러워집니다.\n자연스러운 페이딩과 부드러운 질감이 특징입니다. 어떤 룩에도 풍부한 개성을 더해줍니다.",
            image="product/leather_jacket.webp"
        )
        product4 = Product.objects.create(
            name="윈터 퍼퍼",
            price=200000,
            description="추운 겨울 날씨에 완벽한 보호를 제공하는 윈터 퍼퍼입니다.\n방수 기능이 있는 고밀도 나일론 소재와 보온성이 뛰어난 충전재를 사용하여, 따뜻함과 스타일을 동시에 챙길 수 있습니다.",
        )
        product5 = Product.objects.create(
            name="트렌디 모자",
            price=10000,
            description="어떤 룩에도 쉽게 매치할 수 있는 트렌디 모자입니다.\n가볍고 통기성이 좋은 코튼 소재로 제작되어, 일상에 스타일리시한 포인트를 더해줍니다.",
        )
        product6 = Product.objects.create(
            name="엘리건트 스카프",
            price=30000,
            description="고급스러운 소재와 세련된 디자인의 엘리건트 스카프입니다.\n부드러운 실크 혼방 소재로 제작되어, 목도리로도, 액세서리로도 활용 가능하여 스타일을 다양하게 연출할 수 있습니다.",
        )
        # Set created_at
        product1.created_at = "2021-01-01"
        product1.save()
        product2.created_at = "2022-01-01"
        product2.save()
        product3.created_at = "2023-01-01"
        product3.save()
        product4.created_at = "2024-01-01"
        product4.save()
        product5.created_at = "2024-02-01"
        product5.save()
        product6.created_at = "2024-03-01"
        product6.save()
        # Create product options
        ProductOption.objects.create(product=product1, size="S", stock=10)
        ProductOption.objects.create(product=product1, size="M", stock=20)
        ProductOption.objects.create(product=product1, size="L", stock=30)
        ProductOption.objects.create(product=product2, size="S", stock=10)
        ProductOption.objects.create(product=product2, size="M", stock=20)
        ProductOption.objects.create(product=product2, size="L", stock=30)
        ProductOption.objects.create(product=product3, color="Black", stock=10)
        ProductOption.objects.create(product=product3, color="Brown", stock=20)
        ProductOption.objects.create(product=product4, color="Black", stock=10)
        ProductOption.objects.create(product=product4, size="M", stock=20)
        ProductOption.objects.create(product=product5, color="Black", stock=10)
        ProductOption.objects.create(product=product5, color="Brown", stock=20)
        ProductOption.objects.create(product=product6, color="Black", stock=10)
        ProductOption.objects.create(product=product6, color="Brown", stock=20)
        # Create tags
        tag1 = Tag.objects.create(name="데님")
        tag2 = Tag.objects.create(name="자켓")
        tag3 = Tag.objects.create(name="악세서리")
        tag4 = Tag.objects.create(name="인기")
        tag5 = Tag.objects.create(name="세일")
        # Add tags to products
        product1.tags.add(tag1, tag4, tag5)
        product2.tags.add(tag2)
        product3.tags.add(tag2, tag5)
        product4.tags.add(tag2, tag4)
        product5.tags.add(tag3, tag4)
        product6.tags.add(tag3, tag4)

    def remove_mens_clothes(apps, schema_editor):
        ProductOption.objects.filter(product__name="엘리건트 데님").delete()
        ProductOption.objects.filter(product__name="클래식 슬랙스").delete()
        ProductOption.objects.filter(product__name="럭셔리 가죽 자켓").delete()
        ProductOption.objects.filter(product__name="윈터 퍼퍼").delete()
        ProductOption.objects.filter(product__name="트렌디 모자").delete()
        ProductOption.objects.filter(product__name="엘리건트 스카프").delete()

        Product.objects.filter(name="엘리건트 데님").delete()
        Product.objects.filter(name="클래식 슬랙스").delete()
        Product.objects.filter(name="럭셔리 가죽 자켓").delete()
        Product.objects.filter(name="윈터 퍼퍼").delete()
        Product.objects.filter(name="트렌디 모자").delete()
        Product.objects.filter(name="엘리건트 스카프").delete()

        Tag.objects.filter(name="데님").delete()
        Tag.objects.filter(name="자켓").delete()
        Tag.objects.filter(name="악세서리").delete()
        Tag.objects.filter(name="인기").delete()
        Tag.objects.filter(name="세일").delete()
    

    operations = [
        migrations.RunPython(add_mens_clothes, remove_mens_clothes),
    ]
