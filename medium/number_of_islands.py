from typing import List, Dict, Tuple, Set
from collections import deque

class Solution:

    def bfs(self, grid: List[List[str]], row_index: int, column_index: int, visited: Set[Tuple[int, int]]) -> None:
        
        q = deque()
        q.append((row_index, column_index))

        while len(q) > 0:

            current_row, current_column = q.popleft()
            directions = [[0,1], [0,-1], [1,0], [-1,0]]

            for direction in directions:

                new_row = current_row + direction[0]
                new_column = current_column + direction[1]
    
                if new_row >= 0 and new_row < len(grid) and new_column >= 0 and new_column < len(grid[0]) and grid[new_row][new_column] == '1' and (new_row, new_column) not in visited:
                    visited.add((new_row, new_column))
                    q.append((new_row, new_column))


    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        rows = len(grid)
        columns = len(grid[0])
        visited: Set[Tuple[int, int]] = set()
        islands = 0

        for row_index in range(rows):
            for column_index in range(columns):
                if grid[row_index][column_index] == '1' and (row_index, column_index) not in visited:
                    self.bfs(grid, row_index, column_index, visited)
                    islands += 1

        return islands


# Test cases

matrix_1 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

expected_output_1 = 3

actual_output_1 = Solution().numIslands(matrix_1)

assert actual_output_1 == expected_output_1

matrix_2 = [
    ["1","1","1"],
    ["0","1","0"],
    ["1","1","1"]
]

expected_output_2 = 1

assert Solution().numIslands(matrix_2) == expected_output_2

matriz_3 = [
    ["1","0","1","1","1"],
    ["1","0","1","0","1"],
    ["1","1","1","0","1"]
]

expected_output_3 = 1

assert Solution().numIslands(matriz_3) == expected_output_3

