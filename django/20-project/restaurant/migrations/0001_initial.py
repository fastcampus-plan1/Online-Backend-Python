# Generated by Django 5.0.3 on 2024-03-19 22:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(db_index=True, max_length=100)),
                (
                    "preview_image",
                    models.ImageField(blank=True, null=True, upload_to="article"),
                ),
                ("content", models.TextField()),
                ("show_at_index", models.BooleanField(default=False)),
                ("is_published", models.BooleanField(default=False)),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="생성일"),
                ),
                ("modified_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "칼럼",
                "verbose_name_plural": "칼럼",
            },
        ),
        migrations.CreateModel(
            name="CuisineType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20, verbose_name="이름")),
            ],
            options={
                "verbose_name": "음식 종류",
                "verbose_name_plural": "음식 종류",
            },
        ),
        migrations.CreateModel(
            name="SocialChannel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="이름")),
            ],
            options={
                "verbose_name": "소셜채널",
                "verbose_name_plural": "소셜채널",
            },
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="이름")),
            ],
            options={
                "verbose_name": "태그",
                "verbose_name_plural": "태그",
            },
        ),
        migrations.CreateModel(
            name="RestaurantCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20, verbose_name="이름")),
                (
                    "cuisine_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="restaurant.cuisinetype",
                    ),
                ),
            ],
            options={
                "verbose_name": "가게 카테고리",
                "verbose_name_plural": "가게 카테고리",
            },
        ),
        migrations.CreateModel(
            name="Restaurant",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        db_index=True, max_length=100, verbose_name="이름"
                    ),
                ),
                (
                    "branch_name",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        max_length=100,
                        null=True,
                        verbose_name="지점",
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        db_index=True, max_length=255, verbose_name="주소"
                    ),
                ),
                ("feature", models.CharField(max_length=255, verbose_name="특징")),
                (
                    "is_closed",
                    models.BooleanField(default=False, verbose_name="폐업 여부"),
                ),
                (
                    "latitude",
                    models.DecimalField(
                        db_index=True,
                        decimal_places=12,
                        default="0.0000",
                        max_digits=16,
                        verbose_name="위도",
                    ),
                ),
                (
                    "longitude",
                    models.DecimalField(
                        db_index=True,
                        decimal_places=12,
                        default="0.0000",
                        max_digits=16,
                        verbose_name="경도",
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True,
                        help_text="E.164 포맷",
                        max_length=16,
                        null=True,
                        verbose_name="전화번호",
                    ),
                ),
                (
                    "rating",
                    models.DecimalField(
                        decimal_places=2,
                        default="0.0",
                        max_digits=3,
                        verbose_name="평점",
                    ),
                ),
                (
                    "rating_count",
                    models.PositiveIntegerField(default=0, verbose_name="평가수"),
                ),
                (
                    "start_time",
                    models.TimeField(
                        blank=True, null=True, verbose_name="영업 시작 시간"
                    ),
                ),
                (
                    "end_time",
                    models.TimeField(
                        blank=True, null=True, verbose_name="영업 종료 시간"
                    ),
                ),
                (
                    "last_order_time",
                    models.TimeField(
                        blank=True, null=True, verbose_name="라스트 오더 시간"
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="restaurant.restaurantcategory",
                    ),
                ),
                ("tags", models.ManyToManyField(blank=True, to="restaurant.tag")),
            ],
            options={
                "verbose_name": "레스토랑",
                "verbose_name_plural": "레스토랑",
            },
        ),
        migrations.CreateModel(
            name="RestaurantImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "is_representative",
                    models.BooleanField(default=False, verbose_name="대표 이미지 여부"),
                ),
                (
                    "order",
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name="순서"
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="이름"
                    ),
                ),
                (
                    "image",
                    models.ImageField(upload_to="restaurant", verbose_name="이미지"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, db_index=True, verbose_name="생성일"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, db_index=True, verbose_name="수정일"
                    ),
                ),
                (
                    "restaurant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="restaurant.restaurant",
                    ),
                ),
            ],
            options={
                "verbose_name": "가게 이미지",
                "verbose_name_plural": "가게 이미지",
            },
        ),
        migrations.CreateModel(
            name="RestaurantMenu",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="이름")),
                ("price", models.PositiveIntegerField(default=0, verbose_name="가격")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="restaurant-menu",
                        verbose_name="이미지",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, db_index=True, verbose_name="생성일"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, db_index=True, verbose_name="수정일"
                    ),
                ),
                (
                    "restaurant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="restaurant.restaurant",
                    ),
                ),
            ],
            options={
                "verbose_name": "가게 메뉴",
                "verbose_name_plural": "가게 메뉴",
            },
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="제목")),
                ("author", models.CharField(max_length=100, verbose_name="작성자")),
                (
                    "profile_image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="review-profile",
                        verbose_name="프로필 이미지",
                    ),
                ),
                ("content", models.TextField(verbose_name="내용")),
                ("rating", models.PositiveSmallIntegerField()),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, db_index=True, verbose_name="생성일"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, db_index=True, verbose_name="수정일"
                    ),
                ),
                (
                    "restaurant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="restaurant.restaurant",
                    ),
                ),
                (
                    "social_channel",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="restaurant.socialchannel",
                    ),
                ),
            ],
            options={
                "verbose_name": "리뷰",
                "verbose_name_plural": "리뷰",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="ReviewImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="review")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, db_index=True, verbose_name="생성일"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, db_index=True, verbose_name="수정일"
                    ),
                ),
                (
                    "review",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="restaurant.review",
                    ),
                ),
            ],
            options={
                "verbose_name": "리뷰이미지",
                "verbose_name_plural": "리뷰이미지",
            },
        ),
    ]