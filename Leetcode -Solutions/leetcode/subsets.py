from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        
        def backtrack(start, current):
            subsets.append(current[:])
            
            for i in range(start, len(nums)):
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()
        
        backtrack(0, [])
        return subsets