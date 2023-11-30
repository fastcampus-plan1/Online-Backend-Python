import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)
    less = []
    equal = []
    greater = []

    for element in arr:
        if element < pivot:
            less.append(element)
        elif element == pivot:
            equal.append(element)
        else:
            greater.append(element)     
    return quick_sort(less) + equal + quick_sort(greater)

arr1 = [6, 1, 9, 3, 7, 2, 8, 4, 5]
arr2 = [3, 7, 2, 8, 1, 5, 9, 4, 6]
arr3 = [9, 4, 2, 7, 1, 8, 5, 6, 3]

print(quick_sort(arr1))
print(quick_sort(arr2))
print(quick_sort(arr3))