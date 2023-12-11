from typing import List

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        num_dict = {num: i for i, num in enumerate(nums)}
        for num_to_replace, new_num in operations:
            index = num_dict[num_to_replace]
            nums[index] = new_num
            num_dict[new_num] = index
            del num_dict[num_to_replace]
        return nums
