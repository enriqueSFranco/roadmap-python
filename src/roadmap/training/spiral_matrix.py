from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    row_begin, row_end = 0, len(matrix) - 1
    col_begin, col_end = 0, len(matrix[0]) - 1
    output = []

    while row_begin <= row_end and col_begin <= col_end:
        # travel left to right
        for i in range(col_begin, col_end + 1):
            output.append(matrix[row_begin][i])
        row_begin += 1

        # travel top to bottom
        for i in range(row_begin, row_end):
            output.append(matrix[i][row_begin])
        col_end -= 1

        # travel right to left
        if row_begin <= row_end:
            for i in range(col_end, col_begin - 1, -1):
                output.append(matrix[row_end][i])
            row_end -= 1

        # travel bottom to top
        if col_begin <= col_end:
            for i in range(row_end, row_begin - 1, -1):
                output.append(matrix[i][col_begin])
            col_begin += 1

    return output
