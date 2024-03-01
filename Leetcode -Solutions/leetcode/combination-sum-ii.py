from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # Sort the candidates to handle duplicates
        combinations = []
        self.backtrack(candidates, target, 0, [], combinations)
        return combinations
    
    def backtrack(self, candidates, target, start, current, combinations):
        if target == 0:
            combinations.append(current)
            return
        
        for i in range(start, len(candidates)):
            # Skip duplicates to avoid duplicate combinations
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            
            if candidates[i] > target:
                break
            
            self.backtrack(candidates, target - candidates[i], i + 1, current + [candidates[i]], combinations)