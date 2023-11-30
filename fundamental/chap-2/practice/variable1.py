# 주석을 입력할 수 있습니다.

# 변수의 선언
integer_variable = 42
print(integer_variable) # 42

# 정수와 연산
var = 42
print(var + 10)     # 52
print(var - 5)      # 37
print(var / 10)     # 4.2
print(var // 10)    # 4
print(var % 10)     # 2

# 실수와 연산
var2 = var      # 42
var2 = var / 10 # 4.2

print(var > var2)   # True

var_float = 3.14
print(var_float * 6)    # 18.84
print(var_float / 2)    # 1.57

result = var * 10 + 5   # 425
result = (5 + var) * 10 # 470

# Boolean
is_true = True
is_false = False 

print(is_true and is_true)   # True
print(is_true and is_false)  # False
print(is_false and is_false) # False

print(is_true or is_true)   # True
print(is_true or is_false)  # True
print(is_false or is_false) # False

print((is_false and is_true) or is_true)

