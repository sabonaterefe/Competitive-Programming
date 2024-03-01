from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        
        rows, cols = len(board), len(board[0])
        
        for i in range(rows):
            for j in range(cols):
                if self.dfs(board, i, j, word):
                    return True
        
        return False
    
    def dfs(self, board, i, j, word):
        if len(word) == 0:
            return True
        
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]:
            return False
        
        temp = board[i][j]
        board[i][j] = '#'  # Mark the current cell as visited
        
        # Explore adjacent cells
        found = self.dfs(board, i + 1, j, word[1:]) or \
                self.dfs(board, i - 1, j, word[1:]) or \
                self.dfs(board, i, j + 1, word[1:]) or \
                self.dfs(board, i, j - 1, word[1:])
        
        board[i][j] = temp  # Restore the original value
        
        return found