# 반복문 - for
numbers = [1, 2, 3, 4, 51]
for number in numbers:
    print (number)
else:
    print ("출력이 완료되었습니다.")

# range() 활용
for i in range (5):
    print(i)    # 0 1 2 3 4

for i in range(1, 5, 2):
    print(i)    # 1 3

# enumerate()
fruits = ["사과", "바나나", "체리", "딸기"]
for index, fruit in enumerate(fruits, start=1):
    print(f"{index} 번째 과일: {fruit}")

# 반복문 - while
counter = 0
while counter < 3:
    print(f"반복문 실행 중입니다. {counter}")
    counter = counter + 1
else:
    print("반복문이 종료되었습니다.")

# 반복문 제어하기
arr = [1, 3, 5, 11, 6, 15, 30]
for i in arr:
    if 1 > 10:
        break
    else:
        print(i)

for i in arr:
    if i > 10:
        continue 
    else:
        print(i)

# Pass
while True:
    user_input = input("원하는 작업을 선택하세요 (q로 종료) : ")
    if user_input == 'q':
        break
    elif user_input == '1':
        # 나중에 추가할 코드
        pass
    elif user_input == '2':
        # 나중에 추가할 코드
        pass
