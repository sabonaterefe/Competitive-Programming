from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(string, open, close, n):
            if open == n and close == n:
                result.append(string)
                return

            if open < n:
                backtrack(string + "(", open + 1, close, n)

            if close < open:
                backtrack(string + ")", open, close + 1, n)

        backtrack("", 0, 0, n)
        return result