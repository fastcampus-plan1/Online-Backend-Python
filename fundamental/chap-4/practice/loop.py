# for loop
for i in range(1, 5):
    print(i)

# while
i = 0
while i < 5:
    print (i)
    i = i + 1

# for loop
for i in range(1, 5):
    print(i)
else:
    print ("반복이 완료되었습니다. ")

# 반복문과 조건문
fruits = ["사과", "딸기", "복숭아", "참외"]
for fruit in fruits:
    if fruit == "사과":
        print(f"사과는 맛있습니다.")
    
    print(f"{fruit}이(가) 과일 바구니에 있습니다.")

# 반복문 제어 및 pass 활용하기
while True:
    user_input = input("명령어를 입력해주세요: ")

    if user_input == "exit":
        break
    else:
        pass    # TODO: 차후 개발 예정

# 중첩 반복문: 구구단
# 1단~9단, n * 1 ~ n * 9
for x in range(1, 10):
    for y in range(1, 10):
        print (f"{x} * {y} = {x * y}")

# enumerate 활용하기
fruits = ["Apple", "Banana", "Blueberry", "Peach"]

index = 1
for fruit in fruits:
    print(f"{index}번째 과일은 {fruit} 입니다.")
    index = index + 1

for index, fruit in enumerate(fruits):
    print(f"{index}번째 과일은 {fruit} 입니다.")

# 팩토리얼 구하기
# n! = n * (n - 1) *...* 2 * 1
# 5! = 5 * I * 3 * 2 * 1
num = 10
result = 1
for i in range(1, num + 1):
    result = result * i

print(f"{num}!은 {result} 입니다.")