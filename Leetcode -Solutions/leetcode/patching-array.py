from typing import List

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = 0
        maxReach = 0
        i = 0
        while maxReach < n:
            if i < len(nums) and nums[i] <= maxReach + 1:
                maxReach += nums[i]
                i += 1
            else:
                maxReach += maxReach + 1
                patches += 1

        return patches