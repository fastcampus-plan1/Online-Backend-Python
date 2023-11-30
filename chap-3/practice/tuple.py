my_tuple = ()
my_tuple = (1, )

# 과일 바구니
fruits = ("apple", "banana", "blueberry")
first = fruits[0]
print("first: ", first)

# 패킹과 언패킹
tp = 1, 2, 3
print(tp)

v1, v2, v3 = tp
print(f"{v1}, {v2}, {v3}")

# 값의 교환
a = 10
b = 20
a, b = b, a

tp = (1, 2, 3, 4, 5, 6, 7, 8)
val1, val2, val3, *vals = tp
print(vals)     [4, 5, 6, 7, 8]

vals.append(10)
print(vals)     [4, 5, 6, 7, 8, 10]