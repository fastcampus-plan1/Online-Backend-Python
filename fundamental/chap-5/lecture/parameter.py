# 기본 매개변수
def study (name, language="python"):
    print (f"{name} 님은 {language} 수업 중입니다. ")

# 기본 매개변수 활용
def process_data(data, options=None):
    if options is None:
        options = {
            "name": "Unknown"
        }
    # options 딕셔너리를 사용하여 데이터 처리 로직을 구현
    pass


# 키워드 인자
def greet (name, greeting) :
    print(greeting, name)
    greet(name="Alice", greeting="Hello") # 출력: Hello Alice 
    greet(greeting="Hi", name="Bob") # 출력: Hi Bob

# 가변 인자 리스트
def add_numbers (*args):
    result = 0
    for num in args:
        result += num 
    return result

add_numbers(1)
add_numbers(1, 10, -10, 5)
add_numbers(1, 2, 3, 10, 100, 50)

# 키워드 가변 인자 리스트
def print_kv(**kwargs):
    for key, value in kwargs.items () :
        print (f"{key}: {value}")

print_kv(name = "alpha", age = 10)
print_kv(name = "beta", country = "USA")
print_kv(key = "name")

# 키워드 가변 인자 리스트의 순서
def display_info(name, *args, **kwargs):
    print("Name:", name)
    print("Known Languages:", ', '.join(args))
    for key, value in kwargs.items() :
        print (f"{key}: {value}")