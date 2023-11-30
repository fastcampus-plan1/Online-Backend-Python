empty_list = []
my_list = [1, 2, 3, 4]
my_list[2]      # 3
my_list[2:]     # 3, 4

s = ['l', 'i', 's', 't']
s[1] = 'o'
print(s)    # ['l', 'o', 's', 't']
del s[1]    # ['l', 's', 't']
s.append('i')   # ['l', 's', 't', 'i']

a = [10, 11, 21, 37, 55, 100]
a.sort()    # [10, 11, 21, 37, 55, 100]
a.reverse() # [100, 55, 37, 21, 11, 10]