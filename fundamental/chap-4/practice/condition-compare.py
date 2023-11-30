# 사용자로부터 두 개의 값을 입력받는다.
var1 = input("첫 번째 값을 입력해주세요: ")
var2 = input("두 번째 값을 입력해주세요: ")
# 입력값을 숫자로 변환
num_var1 = int(var1)
num_var2 = int(var2)

# 첫 번째 값이 크다면 "Win", 두 번째 값이 크다면 "Lose"를 출력한다.
# 두 값이 같다면, "Draw"를 출력한다.
if num_var1 > num_var2:
    print("Win")
elif num_var1 < num_var2:
    print("Lose")
else:
    print("Draw")