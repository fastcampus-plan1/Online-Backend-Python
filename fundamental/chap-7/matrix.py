# 이차원 배열 표현
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# O(n^2) 시간 복잡도의 알고리즘 예시: 모든 원소 출력
def print_matrix_elements(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
    print()

# 테스트
print_matrix_elements(matrix)
