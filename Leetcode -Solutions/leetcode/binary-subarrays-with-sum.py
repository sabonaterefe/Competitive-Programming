from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        dict_sum = {0: 1}
        prefixSum = 0
        count = 0
        for num in nums:
            prefixSum += num
            if prefixSum - goal in dict_sum:
                count += dict_sum[prefixSum - goal]
            if prefixSum in dict_sum:
                dict_sum[prefixSum] += 1
            else:
                dict_sum[prefixSum] = 1
        return count