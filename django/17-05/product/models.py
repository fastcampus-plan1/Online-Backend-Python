from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    on_sale = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField("Tag", blank=True)

    class Meta:
        verbose_name = "상품"
        verbose_name_plural = "상품"
        ordering = ("name",)

    def __str__(self):
        return self.name


class ProductOption(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.CharField(max_length=50, blank=True, null=True)
    size = models.CharField(max_length=50, blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "상품 옵션"
        verbose_name_plural = "상품 옵션"
        unique_together = ("product", "color", "size")

    def __str__(self):
        return f"{self.product.name} - {self.color} - {self.size}"


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "태그"
        verbose_name_plural = "태그"
        ordering = ("name",)

    def __str__(self):
        return self.name
