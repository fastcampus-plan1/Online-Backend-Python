import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr      # 원소가 하나면 즉시 반환

    pivot = random.choice(arr) # 무작위로 피벗 선택
    less = []
    equal = []
    greater = []

    for element in arr:
        if element < pivot:
            less.append(element)        # 피벗보다 작은 원소들은 less 배열
        elif element == pivot:
            equal.append(element)      # 피벗과 같은 원소들은 equal 배열
        else:
            greater.append(element)     # 피벗보다 큰 원소들은 greater 배열
    return quick_sort(less) + equal + quick_sort(greater)       # 결합