# 문자열 변수 선언
str_var = "This is my python code."
multi_line = """I'm a developer.
I use python.
Thank you."""

print(str_var)
print(multi_line)

inum1 = 12
inum2 = 34
print(inum1 + inum2)    # 35

snum1 = "12"
snum2 = "34"
print(snum1 + snum2)    # "1234"
print(snum1 * 3)        # "121212"

# 인덱싱
print(str_var[11])  # p
print(str_var[-1])  # .
print(str_var[-5])  # c

# 슬라이싱
print(str_var[11:17])   # python
print(str_var[11:-6])   # python
print(str_var[:10])     # This is my

print(str_var.isalpha())  # True?

str_var_no_space = "Thisismypythoncode."
print(str_var_no_space.isalpha()) # True

num_var = "12"
print(num_var.isdecimal()) # True

num_var = "12 "
print(num_var.isdecimal()) # False

print(str_var.upper)    # THIS IS MY PYTHON CODE.
print(str_var.swapcase) # tHIS IS MY PYTHON CODE.
print(str_var.replace("my", "your"))

# Format String
weather = "흐림"
temp = 15.8
# % code (%s, %d, %f)
res = "오늘 날씨는 %s 입니다. 기온은 %f도 입니다." % (weather, temp)
print(res)

res = "[%s / %f도] 오늘 날씨는 %s 입니다. 기온은 %f도 입니다." % (weather, temp, weather, temp)
print(res)

# .format()
res = "오늘 날씨는 {} 입니다. 기온은 {}도 입니다.".format(weather, temp)
print(res)

res = "[{0} / {1}] 오늘 날씨는 {0} 입니다. 기온은 {1}도 입니다.".format(weather, temp)

# f""
res = f"오늘 날씨는 {weather} 입니다. 기온은 {temp}도 입니다."

# 사용자로부터 값 입력받기
num = input("숫자를 입력해주세요. ")
print(num)

# 이 값을 1 더해서 출력하기
num = int(input) + 1
print(f"입력받은 값에 1을 더하면, {num} 입니다.")