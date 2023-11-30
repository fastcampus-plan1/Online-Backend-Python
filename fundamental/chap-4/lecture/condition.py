# 점수 체크
score = 15
is_passed = False

if score > 10:
    is_passed = True

# 홀수 짝수
num = 11
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 입력에 따른 작업
todo_list = []
choice = input("선택: ")
if choice == "1":
    todo = input("추가할 일: ")
    todo_list.append(todo)
    print(f"{todo} 할 일이 추가되었습니다.")

# 복합 조건문 - elif
score = 8
if score == 10:
    print("You're the Best!")
elif score > 5:
    print("You Passed!")
else:
    print("You Failed..")

# 복합 조건문 - Multi Condition
level = 5
is_passed = True

if level > 2 and is_passed:
    print("You passed!")
elif is_passed:
    print("Your level is not enough")
else:
    print("You should pass")