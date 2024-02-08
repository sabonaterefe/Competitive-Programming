from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = 0
        maxSum = float('-inf') 
        for num in nums:
            currentSum = max(num, currentSum + num)
            maxSum = max(currentSum, maxSum)
        return maxSum