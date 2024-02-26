from typing import List
import math

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        result = nums[0]
        total = nums[0]
        
        for i in range(1, len(nums)):
            total += nums[i]
            result = max(result, math.ceil(total / (i+1)))
        
        return result