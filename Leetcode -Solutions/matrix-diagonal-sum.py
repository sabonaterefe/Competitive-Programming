from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum_diagonal = 0
        n = len(mat)
        
        for i in range(n):
            for j in range(n):
                if i == j or i + j == n - 1:
                    sum_diagonal += mat[i][j]
        
        return sum_diagonal