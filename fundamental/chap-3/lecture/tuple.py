empty_tuple = ()
single_tuple = (1, )
my_tuple = (1, 2, 3, 4)

# 패킹과 언패킹
tp = 1, 2, 3    # 패킹
x, y, z = tp    # 언패킹

x, _, _, y, z = (1, -1, 0, 2, 5)