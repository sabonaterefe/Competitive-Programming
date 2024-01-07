class Solution:
    def longestSubarray(self, nums):
        n = len(nums)
        before = 0
        after = 0
        maxi = 0
        flag = False
        
        for i in range(n):
            if nums[i] == 1:
                if flag:
                    after += 1
                else:
                    before += 1
            else:
                if flag:
                    maxi = max(maxi, before + after)
                    before = after
                    after = 0
                else:
                    flag = True
            
        maxi = max(maxi, before + after)
        
        return maxi - 1 if maxi == n else maxi