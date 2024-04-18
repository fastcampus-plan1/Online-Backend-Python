from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.forms import ValidationError


class Article(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    preview_image = models.ImageField(upload_to="article", null=True, blank=True)
    content = models.TextField()
    show_at_index = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField("생성일", auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "칼럼"
        verbose_name_plural = "칼럼"

    def __str__(self):
        return f"{self.id} - {self.title}"


class Restaurant(models.Model):
    name = models.CharField("이름", max_length=100, db_index=True)
    branch_name = models.CharField(
        "지점", max_length=100, db_index=True, null=True, blank=True
    )
    description = models.TextField("설명", null=True, blank=True)
    address = models.CharField("주소", max_length=255, db_index=True)
    feature = models.CharField("특징", max_length=255)
    is_closed = models.BooleanField("폐업 여부", default=False)
    latitude = models.DecimalField(
        "위도",
        max_digits=16,
        decimal_places=12,
        db_index=True,
        default="0.0000",
    )
    longitude = models.DecimalField(
        "경도",
        max_digits=16,
        decimal_places=12,
        db_index=True,
        default="0.0000",
    )
    phone = models.CharField(
        "전화번호", max_length=16, help_text="E.164 포맷", blank=True, null=True
    )
    rating = models.DecimalField("평점", max_digits=3, decimal_places=2, default="0.0")
    rating_count = models.PositiveIntegerField("평가수", default=0)
    start_time = models.TimeField("영업 시작 시간", null=True, blank=True)
    end_time = models.TimeField("영업 종료 시간", null=True, blank=True)
    last_order_time = models.TimeField("라스트 오더 시간", null=True, blank=True)
    category = models.ForeignKey(
        "RestaurantCategory", on_delete=models.SET_NULL, blank=True, null=True
    )
    tags = models.ManyToManyField("Tag", blank=True)

    class Meta:
        verbose_name = "레스토랑"
        verbose_name_plural = "레스토랑"

    def __str__(self):
        return f"{self.name} {self.branch_name}" if self.branch_name else f"{self.name}"


class CuisineType(models.Model):
    name = models.CharField("이름", max_length=20)

    class Meta:
        verbose_name = "음식 종류"
        verbose_name_plural = "음식 종류"

    def __str__(self):
        return self.name


class RestaurantCategory(models.Model):
    name = models.CharField("이름", max_length=20)
    cuisine_type = models.ForeignKey(
        "CuisineType",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "가게 카테고리"
        verbose_name_plural = "가게 카테고리"

    def __str__(self):
        return self.name


class RestaurantImage(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    is_representative = models.BooleanField("대표 이미지 여부", default=False)
    order = models.PositiveIntegerField("순서", null=True, blank=True)
    name = models.CharField("이름", max_length=100, null=True, blank=True)
    image = models.ImageField("이미지", max_length=100, upload_to="restaurant")
    created_at = models.DateTimeField("생성일", auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField("수정일", auto_now=True, db_index=True)

    class Meta:
        verbose_name = "가게 이미지"
        verbose_name_plural = "가게 이미지"

    def __str__(self):
        return f"{self.id}:{self.image}"

    def clean(self):
        images = self.restaurant.restaurantimage_set.filter(is_representative=True)
        if self.is_representative and images.exclude(id=self.id).count() > 0:
            raise ValidationError("대표 이미지는 1개만 지정 가능합니다.")


class RestaurantMenu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField("이름", max_length=100)
    price = models.PositiveIntegerField("가격", default=0)
    image = models.ImageField(
        "이미지", upload_to="restaurant-menu", null=True, blank=True
    )
    created_at = models.DateTimeField("생성일", auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField("수정일", auto_now=True, db_index=True)

    class Meta:
        verbose_name = "가게 메뉴"
        verbose_name_plural = "가게 메뉴"

    def __str__(self):
        return self.name


class Review(models.Model):
    title = models.CharField("제목", max_length=100)
    author = models.CharField("작성자", max_length=100)
    profile_image = models.ImageField(
        "프로필 이미지", upload_to="review-profile", blank=True, null=True
    )
    content = models.TextField("내용")
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    social_channel = models.ForeignKey(
        "SocialChannel", on_delete=models.SET_NULL, blank=True, null=True
    )
    created_at = models.DateTimeField("생성일", auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField("수정일", auto_now=True, db_index=True)

    class Meta:
        verbose_name = "리뷰"
        verbose_name_plural = "리뷰"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.author}:{self.title}"

    @property
    def restaurant_name(self):
        return self.restaurant.name

    @property
    def content_partial(self):
        return self.content[:20]


class ReviewImage(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(max_length=100, upload_to="review")
    created_at = models.DateTimeField("생성일", auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField("수정일", auto_now=True, db_index=True)

    class Meta:
        verbose_name = "리뷰이미지"
        verbose_name_plural = "리뷰이미지"

    def __str__(self):
        return f"{self.id}:{self.image}"


class SocialChannel(models.Model):
    name = models.CharField("이름", max_length=100)

    class Meta:
        verbose_name = "소셜채널"
        verbose_name_plural = "소셜채널"

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField("이름", max_length=100)

    class Meta:
        verbose_name = "태그"
        verbose_name_plural = "태그"

    def __str__(self):
        return self.name
