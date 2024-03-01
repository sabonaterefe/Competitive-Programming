class Solution:
    def solveNQueens(self, n):
        def backtrack(row, cols, diagonals, anti_diagonals):
            if row == n:
                solutions.append(board[:])
                return

            for col in range(n):
                diagonal_id = row - col
                anti_diagonal_id = row + col

                if col not in cols and diagonal_id not in diagonals and anti_diagonal_id not in anti_diagonals:
                    board[row] = col
                    cols.add(col)
                    diagonals.add(diagonal_id)
                    anti_diagonals.add(anti_diagonal_id)

                    backtrack(row + 1, cols, diagonals, anti_diagonals)

                    cols.remove(col)
                    diagonals.remove(diagonal_id)
                    anti_diagonals.remove(anti_diagonal_id)

        solutions = []
        board = [-1] * n
        cols = set()
        diagonals = set()
        anti_diagonals = set()

        backtrack(0, cols, diagonals, anti_diagonals)

        formatted_solutions = []
        for solution in solutions:
            formatted_solution = []
            for col in solution:
                formatted_solution.append('.' * col + 'Q' + '.' * (n - col - 1))
            formatted_solutions.append(formatted_solution)

        return formatted_solutions