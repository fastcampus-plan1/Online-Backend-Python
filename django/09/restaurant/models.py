from django.db import models

class RestaurantCategory(models.Model):
    name = models.CharField("이름", max_length=20)

    class Meta:
        verbose_name = "가게 카테고리"
        verbose_name_plural = "가게 카테고리"

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField("이름", max_length=100, db_index=True)
    category = models.ForeignKey("RestaurantCategory", on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField("주소", max_length=255)
    phone = models.CharField("전화번호", max_length=16, help_text="E.164 포맷", db_index=True)
    image = models.ImageField(upload_to='restaurants/', null=True, blank=True)
    start_time = models.TimeField("영업 시작 시간", null=True, blank=True)
    end_time = models.TimeField("영업 종료 시간", null=True, blank=True)
    latitude = models.DecimalField("위도", max_digits=9, decimal_places=6, db_index=True)
    longitude = models.DecimalField("경도", max_digits=9, decimal_places=6, db_index=True)
    rating = models.DecimalField("별점", max_digits=3, decimal_places=2, db_index=True)
    rating_count = models.PositiveIntegerField("별점 개수")
    keywords = models.ManyToManyField("Keyword", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        verbose_name = "가게"
        verbose_name_plural = "가게"
        ordering = ["-rating"]

    def __str__(self):
        return self.name


class RestaurantStatistics(models.Model):
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE)
    view_count = models.PositiveIntegerField(default=0)
    like_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        verbose_name = "가게 통계"
        verbose_name_plural = "가게 통계"

    def __str__(self):
        return self.restaurant.name
    


class Keyword(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "키워드"
        verbose_name_plural = "키워드"

    def __str__(self):
        return self.name