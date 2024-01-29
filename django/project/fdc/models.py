from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    preview_content = models.TextField()
    url = models.URLField()
    image = models.ImageField(upload_to="articles_image")
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        verbose_name = "기사"
        verbose_name_plural = "기사"
        ordering = ["-created_at"]


class CuisineType(models.Model):
    name = models.CharField("이름", max_length=20)

    class Meta:
        verbose_name = "음식 종류"
        verbose_name_plural = "음식 종류"


class RestaurantCategory(models.Model):
    name = models.CharField("이름", max_length=20)
    cuisine_type = models.ForeignKey(
        "CuisineType", on_delete=models.SET_NULL, blank=True, null=True
    )

    class Meta:
        verbose_name = "가게 카테고리"
        verbose_name_plural = "가게 카테고리"


class Restaurant(models.Model):
    category = models.ForeignKey(
        "RestaurantCategory", on_delete=models.SET_NULL, blank=True, null=True
    )
    name = models.CharField("이름", max_length=100)
    area_name = models.CharField("지역 이름", max_length=100)
    address = models.CharField("주소", max_length=255)
    phone = models.CharField("전화번호", max_length=16, help_text="E.164 포맷")
    image_url = models.URLField("이미지 URL", blank=True, max_length=255)
    rating = models.DecimalField("별점", max_digits=3, decimal_places=2)
    rating_count = models.PositiveIntegerField("별점 개수")
    start_time = models.TimeField("영업 시작 시간", null=True, blank=True)
    end_time = models.TimeField("영업 종료 시간", null=True, blank=True)
    latitude = models.DecimalField(
        "위도", db_index=True, max_digits=9, decimal_places=6
    )
    longitude = models.DecimalField(
        "경도", db_index=True, max_digits=9, decimal_places=6
    )
    keywords = models.ManyToManyField("Keyword", blank=True)
    tags = models.ManyToManyField("Tag", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        verbose_name = "가게"
        verbose_name_plural = "가게"
        ordering = ["-rating"]

    def __str__(self):
        return self.name

    def has_image(self):
        return self.image_url != ""


class Keyword(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "키워드"
        verbose_name_plural = "키워드"


class RestaurantImage(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    is_representative = models.BooleanField(default=False)
    order = models.PositiveIntegerField(null=True, blank=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(max_length=100, upload_to="restaurant_images")
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        verbose_name = "가게 이미지"
        verbose_name_plural = "가게 이미지"


class RestaurantMenu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        verbose_name = "가게 메뉴"
        verbose_name_plural = "가게 메뉴"


class RestaurantStatistics(models.Model):
    view_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "가게통계"
        verbose_name_plural = "가게통계"


class Review(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = models.TextField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    social_channel = models.ForeignKey(
        "SocialChannel", on_delete=models.SET_NULL, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        verbose_name = "리뷰"
        verbose_name_plural = "리뷰"
        ordering = ["-created_at"]


class ReviewImage(models.Model):
    image = models.ImageField(max_length=100, upload_to="review_images")
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        verbose_name = "리뷰이미지"
        verbose_name_plural = "리뷰이미지"


class SocialChannel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "소셜채널"
        verbose_name_plural = "소셜채널"


class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "태그"
        verbose_name_plural = "태그"
