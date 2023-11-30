# 함수의 선언
def func (name):
    print(f"This is Function. Hello {name}!")

func("Park")

# 함수의 활용
def sum(num1, num2):
    return num1 + num2

def div (num1, num2):
    if num2 == 0:
        return 0
    
    print("Divisioning...")
    return num1 / num2

result = sum(3, 5)
print(result)

result_div = div(3, 2)
print(result_div)

result_div = div(3, 0)
print(result_div)