from decimal import Decimal

from django.core.files.base import ContentFile
from django.test import TestCase

from restaurant.models import (
    Article,
    CuisineType,
    Restaurant,
    RestaurantCategory,
    RestaurantImage,
    RestaurantMenu,
    Review,
    ReviewImage,
    SocialChannel,
    Tag,
)


class ArticleModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Article.objects.create(
            title="테스트 칼럼 제목",
            content="테스트 칼럼 내용",
            preview_image=ContentFile(
                b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A", name="test-image.png"
            ),
            show_at_index=True,
            is_published=True,
        )

    def test_content(self):
        article = Article.objects.get(id=1)
        expected_data = article
        self.assertEqual(expected_data.title, "테스트 칼럼 제목")
        self.assertEqual(expected_data.content, "테스트 칼럼 내용")
        self.assertEqual(expected_data.show_at_index, True)
        self.assertEqual(expected_data.is_published, True)
        self.assertTrue(
            expected_data.preview_image.name.startswith("article/test-image")
        )


class RestaurantModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Restaurant.objects.create(
            name="테스트 식당",
            address="서울시 강남구 역삼동 123-456",
            phone="+82212345678",
            description="테스트 식당 설명",
            latitude=37.123456,
            longitude=127.123456,
            rating=4.5,
            rating_count=1_000,
            is_closed=True,
        )

    def test_content(self):
        restaurant = Restaurant.objects.get(id=1)
        expected_data = restaurant
        self.assertEqual(expected_data.name, "테스트 식당")
        self.assertEqual(expected_data.address, "서울시 강남구 역삼동 123-456")
        self.assertEqual(expected_data.phone, "+82212345678")
        self.assertEqual(expected_data.description, "테스트 식당 설명")
        self.assertEqual(expected_data.latitude, Decimal("37.12345600000"))
        self.assertEqual(expected_data.longitude, Decimal("127.12345600000"))
        self.assertEqual(expected_data.rating, 4.5)
        self.assertEqual(expected_data.rating_count, 1_000)
        self.assertEqual(expected_data.is_closed, True)


class CuisineTypeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        CuisineType.objects.create(name="한식")

    def test_content(self):
        cuisine_type = CuisineType.objects.get(id=1)
        expected_data = cuisine_type
        self.assertEqual(expected_data.name, "한식")


class RestaurantCategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        RestaurantCategory.objects.create(name="카페")

    def test_content(self):
        restaurant_category = RestaurantCategory.objects.get(id=1)
        expected_data = restaurant_category
        self.assertEqual(expected_data.name, "카페")


class RestaurantImageModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        restaurant = Restaurant.objects.create(name="테스트 식당")
        RestaurantImage.objects.create(
            restaurant=restaurant,
            image=ContentFile(
                b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A", name="test-image.png"
            ),
        )

    def test_content(self):
        restaurant_image = RestaurantImage.objects.get(id=1)
        expected_data = restaurant_image
        self.assertEqual(expected_data.restaurant.name, "테스트 식당")
        self.assertTrue(expected_data.image.name.startswith("restaurant/test-image"))


class RestaurantMenuModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        restaurant = Restaurant.objects.create(name="테스트 식당")
        RestaurantMenu.objects.create(
            restaurant=restaurant,
            name="테스트 메뉴",
            price=15_000,
        )

    def test_content(self):
        restaurant_menu = RestaurantMenu.objects.get(id=1)
        expected_data = restaurant_menu
        self.assertEqual(expected_data.restaurant.name, "테스트 식당")
        self.assertEqual(expected_data.name, "테스트 메뉴")
        self.assertEqual(expected_data.price, 15_000)


class ReviewModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        restaurant = Restaurant.objects.create(name="테스트 식당")
        Review.objects.create(
            restaurant=restaurant,
            rating=4,
            content="테스트 리뷰 내용",
        )

    def test_content(self):
        review = Review.objects.get(id=1)
        expected_data = review
        self.assertEqual(expected_data.restaurant.name, "테스트 식당")
        self.assertEqual(expected_data.rating, 4)
        self.assertEqual(expected_data.content, "테스트 리뷰 내용")


class ReviewImageModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        restaurant = Restaurant.objects.create(name="테스트 식당")
        review = Review.objects.create(
            restaurant=restaurant,
            rating=4,
            content="테스트 리뷰 내용",
        )
        ReviewImage.objects.create(
            review=review,
            image=ContentFile(
                b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A", name="test-image.png"
            ),
        )

    def test_content(self):
        review_image = ReviewImage.objects.get(id=1)
        expected_data = review_image
        self.assertEqual(expected_data.review.restaurant.name, "테스트 식당")
        self.assertTrue(expected_data.image.name.startswith("review/test-image"))


class SocialChannelModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        SocialChannel.objects.create(name="Instagram")

    def test_content(self):
        social_channel = SocialChannel.objects.get(id=1)
        expected_data = social_channel
        self.assertEqual(expected_data.name, "Instagram")


class TagModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(name="맛집")

    def test_content(self):
        tag = Tag.objects.get(id=1)
        expected_data = tag
        self.assertEqual(expected_data.name, "맛집")
