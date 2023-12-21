from typing import List

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_zeros = 0
        right_ones = sum(nums)
        max_score = left_zeros + right_ones
        max_indices = [0]

        for i in range(n):
            if nums[i] == 0:
                left_zeros += 1
            else:
                right_ones -= 1

            score = left_zeros + right_ones

            if score > max_score:
                max_score = score
                max_indices = [i + 1]
            elif score == max_score:
                max_indices.append(i + 1)

        return max_indices