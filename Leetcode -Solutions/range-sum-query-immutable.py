from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_sum = self.calculate_prefix_sum()

    def calculate_prefix_sum(self) -> List[int]:
        prefix_sum = [0]
        for num in self.nums:
            prefix_sum.append(prefix_sum[-1] + num)
        return prefix_sum

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]