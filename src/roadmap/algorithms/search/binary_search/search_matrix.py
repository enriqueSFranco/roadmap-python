from typing import List

def search_matrix(matrix:List[List[int]], target:int) -> bool:
    if not matrix or not matrix[0]:
        return False

    m = len(matrix) # total de filas
    n = len(matrix[0]) # total de columnas

    # aplicamos busqueda binaria
    left = 0
    right = m * n - 1

    while left <= right:
        mid = left + ((right - left) // 2)
        #pasamos el mid a indices de una matriz (row, col)
        row = mid // n
        col = mid % n
        if matrix[row][col] == target:
            return True
        if matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

# matriz 2 * 4
matrix = [
  [-1,  0,  1],
  [1,  2,  3],
  [4,  5,  6],
  [7,  8,  9]
]

print(search_matrix(matrix, -1))