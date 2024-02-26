from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        result = [-1] * n * 2

        nums += nums

        for i in range(2 * n - 1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()

            if stack:
                result[i % n] = stack[-1]

            stack.append(nums[i])

        return result[:n]