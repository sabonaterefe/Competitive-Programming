from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = windowSum = sum(nums[:k])
        
        for i in range(k, len(nums)):
            windowSum = windowSum - nums[i - k] + nums[i]
            maxSum = max(maxSum, windowSum)
        
        return maxSum / k