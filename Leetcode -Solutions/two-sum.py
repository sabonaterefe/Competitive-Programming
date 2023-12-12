from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_dict = {}
        for i, num in enumerate(nums):
            if target - num in complement_dict:
                return [complement_dict[target - num], i]
            complement_dict[num] = i
        return []
