from typing import List

"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

"""


def numIslands(grid: List[List[str]]) -> int:
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])

    def dfs(grid: List[List[str]], r: int, c: int):
        # verificamos no salirnos de los limites de la grid o que el valor de una celda sea cero (0)
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
            return

        # marcamos la celda como visitada
        grid[r][c] == "0"

        dfs(grid, r + 1, c)  # bottom
        dfs(grid, r - 1, c)  # top
        dfs(grid, r, c + 1)  # rigth
        dfs(grid, r, c - 1)  # left

    island_counter = 0
    # iterar sobre cada celda
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                island_counter += 1
                dfs(grid, r, c)

    return island_counter
