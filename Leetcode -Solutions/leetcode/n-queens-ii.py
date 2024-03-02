class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count = 0
        self.solveNQueens(n, 0, set(), set(), set())
        return self.count

    def solveNQueens(self, n, row, queens, diagonals, anti_diagonals):
        if row == n:
            self.count += 1
            return

        for col in range(n):
            if col in queens or (row + col) in diagonals or (row - col) in anti_diagonals:
                continue

            queens.add(col)
            diagonals.add(row + col)
            anti_diagonals.add(row - col)

            self.solveNQueens(n, row + 1, queens, diagonals, anti_diagonals)

            queens.remove(col)
            diagonals.remove(row + col)
            anti_diagonals.remove(row - col)