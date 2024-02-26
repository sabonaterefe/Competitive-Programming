from typing import List

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_max = [0] * n
        col_max = [0] * n
        max_total_sum = 0
        for r in range(n):
            for c in range(n):
                row_max[r] = max(row_max[r], grid[r][c])
                col_max[c] = max(col_max[c], grid[r][c])
        for r in range(n):
            for c in range(n):
                max_possible_height = min(row_max[r], col_max[c])
                max_total_sum += max_possible_height - grid[r][c]

        return max_total_sum