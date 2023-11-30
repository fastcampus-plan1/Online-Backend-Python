def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid  # 찾은 경우 해당 인덱스 반환
        elif mid_value < target:
            low = mid + 1  # 중간 값이 목표보다 작으면 오른쪽 반으로 탐색
        else:
            high = mid - 1  # 중간 값이 목표보다 크면 왼쪽 반으로 탐색

    return -1  # 목표값이 배열에 없는 경우

# 테스트
sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_value = 7
result = binary_search(sorted_array, target_value)
print(f"배열 {sorted_array}에서 {target_value}의 인덱스: {result}")
