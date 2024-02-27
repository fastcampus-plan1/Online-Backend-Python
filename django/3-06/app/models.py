from django.db import models

class Product(models.Model):
    name = models.CharField("상품 이름", max_length=100)
    price = models.DecimalField("가격", max_digits=10, decimal_places=2)
    description = models.TextField("설명")
    image = models.ImageField("이미지", upload_to="products/", blank=True, null=True)
    created_at = models.DateTimeField("생성일", auto_now_add=True)
    updated_at = models.DateTimeField("수정일", auto_now=True)
