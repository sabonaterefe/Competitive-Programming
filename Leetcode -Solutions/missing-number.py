class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)
        n=len(nums_set)
        for i in range(n+1):
            if i not in nums_set:
                return i

        