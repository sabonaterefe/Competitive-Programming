from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        nums.sort()  # Sorting the input array to handle duplicates
        
        def backtrack(start, current):
            subsets.append(current[:])
            
            for i in range(start, len(nums)):
                # Skipping duplicates
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()
        
        backtrack(0, [])
        return subsets