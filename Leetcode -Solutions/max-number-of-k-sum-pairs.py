class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        operations=0
        nums.sort()
        i =0
        j=len(nums)-1
        while i<j:
            sum_two = nums[i]+nums[j]
            if sum_two==k:
                operations+=1
                i+=1
                j-=1
            elif sum_two<k:
                i+=1
            else:
                j-=1
        return operations
        