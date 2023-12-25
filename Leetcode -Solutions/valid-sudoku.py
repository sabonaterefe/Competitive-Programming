from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid_unit(unit):
            unit = [i for i in unit if i != '.']
            return len(set(unit)) == len(unit)

        for i in range(9):
            if not is_valid_unit(board[i]) or not is_valid_unit([board[j][i] for j in range(9)]):
                return False

        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not is_valid_unit([
                    board[x][y]
                    for x in range(i, i + 3)
                    for y in range(j, j + 3)
                ]):
                    return False

        return True