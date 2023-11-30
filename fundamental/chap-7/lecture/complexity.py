# O(n) 시간 복잡도의 알고리즘 예시: 리스트의 모든 요소 출력
def print_list_elements(lst):
    for element in lst:
        print(element, end=" ")
    print()

# 테스트
my_list = [1, 2, 3, 4, 5]
print_list_elements(my_list)

# O(n^2)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 0(n^2) 시간 복잡도의 알고리즘 예시: 모든 원소 출력
def print_matrix_elements (matrix):
    for row in matrix:
        for element in row:
            print (element, end="")
    print ()