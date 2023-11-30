my_dict = {}
my_dict["key"] = "value"

print(my_dict)

person = {"name": "홍길동", "age": "30", "고향": "서울"}
name = person["name"]

print(f"이름은 {person['name']}, 나이는 {person['age']}, 고향은 {person['city']} 입니다.")

country = person.get("country", "알 수 없음")
print(f"국적은 {country} 입니다.")

person = {"name": "홍길동", "age": "30", "고향": "서울"}
person_detail = {"country": "대한민국", "married": True}

person.update(person_detail)

country = person.get("country", "알 수 없음")
print(f"국적은 {country} 입니다.")

print("Before ", person.keys())
del person["married"]

print("After ", person.keys())
print("After ", person.keys())