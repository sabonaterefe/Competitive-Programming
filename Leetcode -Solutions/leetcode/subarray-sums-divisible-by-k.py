from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        div_dict = {0: 1}
        count = 0

        for num in nums:
            prefixSum = (prefixSum + num) % k
            if prefixSum in div_dict:
                count += div_dict[prefixSum]
                div_dict[prefixSum] += 1
            else:
                div_dict[prefixSum] = 1

        return count