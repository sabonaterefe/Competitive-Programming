from math import floor
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            if nums.count(nums[i])>math.floor(len(nums)//3):
                result.append(nums[i])
        return list(set(result))
        