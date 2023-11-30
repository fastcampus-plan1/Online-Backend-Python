my_list = [30, 40, 50]
my_list.append(10)
my_list.append(15)
my_list.append(20)
print(my_list)      # [30, 40, 50, 10, 15, 20]

sliced = my_list[3:]
print("Sliced : ", sliced)

fruits = ["banana", "apple", "blueberry", "cherry"]

# 바나나가 포함되어 있나요?
is_banana_included = "banana" in fruits
print("Is banana included?", is_banana_included)    # True

# 체리는 몇 번째에 있나요?
index_cherry = fruits.index("cherry")
print("Cherry is ", index_cherry)

# 리스트의 정렬
numbers = [4, 2, 1, 3, 8, 6, 7, 5]
print("Unsorted ", numbers)

numbers.sort()
print("Sorted ", numbers)

numbers.sort(reverse=True)
print("Sorted (Reverse) ", numbers)

# 리스트의 요소 추가 및 제거
my_list = []
my_list.append(10)
my_list.append(11)
my_list.append(12)
print(my_list)

my_list.extend([13, 14, 15])
print(my_list)

my_list.append([16, 17])
print(my_list)

print(my_list[-1])

# 리스트의 연산 (*, +)
my_list = [10, 11, 12, 13, 14, 15]
new_list = my_list + [0, 1, 2]
print(new_list)

multi_list = [0, 1, 3] * 3
print(multi_list)

max_value = max(my_list)
min_value = min(my_list)
print(f"최대 값은 {max_value}, 최소 값은 {min_value} 입니다.")