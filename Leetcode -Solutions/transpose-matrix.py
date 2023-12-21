from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        column = len(matrix[0])
        modified_matrix = [[0] * row for _ in range(column)]

        for i in range(row):
            for j in range(column):
                modified_matrix[j][i] = matrix[i][j]

        return modified_matrix