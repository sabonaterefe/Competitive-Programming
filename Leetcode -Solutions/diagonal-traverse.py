from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        result = []
        row, col = 0, 0
        direction = 1

        for _ in range(m * n):
            result.append(mat[row][col])
            row -= direction
            col += direction

            if row >= m:
                row = m - 1
                col += 2
                direction = -direction
            elif col >= n:
                col = n - 1
                row += 2
                direction = -direction
            elif row < 0:
                row = 0
                direction = -direction
            elif col < 0:
                col = 0
                direction = -direction

        return result