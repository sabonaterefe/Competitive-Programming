from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        
        def backtrack(combination, num, remaining):
            if remaining == 0:
                combinations.append(combination)
                return
            
            if num > n or remaining < 0:
                return
            
            backtrack(combination + [num], num + 1, remaining - 1)
            backtrack(combination, num + 1, remaining)
        
        backtrack([], 1, k)
        return combinations