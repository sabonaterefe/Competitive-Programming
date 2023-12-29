class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        sorted_list =nums.sort(reverse=True)
        n= len(nums)
        count = 0
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                count+=i+1
        return count

        