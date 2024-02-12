from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums) % p
        if target == 0:
            return 0

        prefix_remainder_dic = {0: -1}
        remainder = 0
        min_length = len(nums)

        for i, num in enumerate(nums):
            remainder = (remainder + num) % p
            complement = (remainder - target) % p

            if complement in prefix_remainder_dic:
                length = i - prefix_remainder_dic[complement]
                min_length = min(min_length, length)

            prefix_remainder_dic[remainder] = i

        return -1 if min_length == len(nums) else min_length