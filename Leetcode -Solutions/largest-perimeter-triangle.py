from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        largest_perimeter = 0

        for i in range(len(nums) - 1, 1, -1):
            if nums[i - 2] + nums[i - 1] > nums[i]:
                largest_perimeter = nums[i - 2] + nums[i - 1] + nums[i]
                break

        return largest_perimeter