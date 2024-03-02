class Solution:
    def solveSudoku(self, board):
        self.solve(board)

    def solve(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in '123456789':
                        if self.isValid(board, i, j, num):
                            board[i][j] = num
                            if self.solve(board):
                                return True
                            board[i][j] = '.'  # backtrack if the current number doesn't lead to a solution
                    return False  # no valid number found for the current cell
        return True  # all cells are filled, a solution is found

    def isValid(self, board, row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num or board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
                return False
        return True