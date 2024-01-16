from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums, k):
        mp = defaultdict(int)
        
        # Replace odd with 1 and even with 0
        for i, num in enumerate(nums):
            if num % 2:
                nums[i] = 1
            else:
                nums[i] = 0
        
        mp[0] = 1
        prefix_sum = 0
        count = 0
        
        for num in nums:
            prefix_sum += num
            count += mp[prefix_sum - k]
            mp[prefix_sum] += 1
        
        return count