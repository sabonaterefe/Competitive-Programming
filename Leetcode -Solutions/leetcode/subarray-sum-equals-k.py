class Solution:
    def subarraySum(self, nums, k):
        count = 0
        prefix_sum = 0
        sum_dict = {0: 1}
        
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in sum_dict:
                count += sum_dict[prefix_sum - k]
            if prefix_sum in sum_dict:
                sum_dict[prefix_sum] += 1
            else:
                sum_dict[prefix_sum] = 1
        
        return count