def bubble_sort(arr):
    n = len (arr)
    for i in range(n):
        # 매 정렬에서 가장 큰 원소가 맨 뒤로 이동하므로,
        # 마지막 1 번째의 원소는 정렬되어 있음
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # 두 원소를 교환
                arr[j], arr[j + 1] = arr[j + 1], arr[j]