
from django.db.models import Q
from django.core.exceptions import (
    ObjectDoesNotExist,
    MultipleObjectsReturned,
)

from restaurant.models import Restaurant

# Restaurant 모델의 모든 row를 가져오기
restaurants = Restaurant.objects.all()

print("모든 레스토랑")
print(restaurants)
print(restaurants.count())
print("=====================")

# 쿼리셋을 리스트처럼 사용하기
for restaurant in restaurants:
    print(restaurant.name, restaurant.address)
# 앞 다섯 개 객체 가져오기
first_five_restaurants = Restaurant.objects.all()[:5]
# 6번째부터 10번째 객체 가져오기
next_five_restaurants = Restaurant.objects.all()[5:10]

print("앞 다섯 개 레스토랑")
print(first_five_restaurants)
print("다음 다섯 개 레스토랑")
print(next_five_restaurants)
print("=====================")


try:
    # ‘맛집'이라는 이름의 레스토랑 객체를 가져옵니다.
    restaurant = Restaurant.objects.get(name="맛집")
    # 가져온 객체의 정보를 출력합니다.
    print(f"레스토랑 이름: {restaurant.name}")
    print(f"주소: {restaurant.address}")
    print(f"별점: {restaurant.rating}")
except ObjectDoesNotExist:
    # 해당 이름을 가진 레스토랑이 존재하지 않을 때
    print("해당 레스토랑이 존재하지 않습니다.")
except MultipleObjectsReturned:
    # 해당 이름을 가진 레스토랑이 여러 개 있을 때
    print("해당 레스토랑이 여러 개 존재합니다.")
print("=====================")



# 특정 카테고리 (예: "한식")에 속하는 레스토랑 찾기
korean_restaurants = Restaurant.objects.filter(
    category="한식"
)

# 특정 카테고리 (예: "한식")에 속하지 않는 레스토랑 찾기
non_korean_restaurants = Restaurant.objects.exclude(
    category="한식"
)

# 특정 카테고리 (예: "한식")에 속하는 5점 레스토랑 찾기
korean_five_star_restaurants = Restaurant.objects.filter(
    category="한식", 
    rating=5
)

print("한식 레스토랑")
print(korean_restaurants)
print("한식이 아닌 레스토랑")
print(non_korean_restaurants)
print("한식 5점 레스토랑")
print(korean_five_star_restaurants)
print("=====================")

# 주소가 지정 된 레스토랑 찾기 (address 필드가 NULL이 아닌 경우)
restaurants_without_address = Restaurant.objects.filter(
    address__isnull=False,
)

# 별점이 3점 이상 4점 미만인 레스토랑 찾기
restaurants_in_rating_range = Restaurant.objects.filter(
    rating__gte=3, 
    rating__lt=4,
)

print("주소가 있는 레스토랑")
print(restaurants_without_address)
print("별점이 3점 이상 4점 미만인 레스토랑")
print(restaurants_in_rating_range)
print("=====================")

# 한식 또는 중식이면서, 별점이 4점 이상인 레스토랑 찾기
restaurants = Restaurant.objects.filter(
    Q(category="한식") | Q(category="중식"),
    rating__gte=4
)

# 한식이 아니면서 별점이 4점 이이상인 레스토랑 찾기
restaurants = Restaurant.objects.filter(
    ~Q(category="한식") & Q(rating__gte=4)
)

print("한식 또는 중식이면서, 별점이 4점 이상인 레스토랑")
print(restaurants)
print("한식이 아니면서 별점이 4점 이상인 레스토랑")
print(restaurants)
print("=====================")