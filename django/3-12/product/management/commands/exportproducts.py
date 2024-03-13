from django.core.management.base import BaseCommand

from product.models import Product

class Command(BaseCommand):
    help = "모든 상품을 출력합니다."

    def add_arguments(self, parser):
        parser.add_argument(
            "--separator",
            default=" ",
            type=str,
            help="상품 정보 사이에 넣을 구분자를 지정합니다. 기본값은 공백입니다.",
        )

    def handle(self, *args, **options):
        sep = options["separator"]
        for p in Product.objects.order_by("id"):
            self.stdout.write(
                sep.join([str(p.id), p.name, str(p.price), "1" if p.on_sale else "0"])
            )