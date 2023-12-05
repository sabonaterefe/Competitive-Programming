from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        index = -1

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                count += 1
                index = i
                if count > 1:
                    return False

        if count == 0 or count == 1:
            if index == -1 or index == 0 or index == len(nums) - 2 or nums[index - 1] <= nums[index + 1] or nums[index] <= nums[index + 2]:
                return True

        return False