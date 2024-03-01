from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        
        def backtrack(start, current_sum, current_combination):
            if current_sum == target:
                combinations.append(current_combination[:])
                return
            
            if current_sum > target:
                return
            
            for i in range(start, len(candidates)):
                current_combination.append(candidates[i])
                backtrack(i, current_sum + candidates[i], current_combination)
                current_combination.pop()
        
        backtrack(0, 0, [])
        return combinations