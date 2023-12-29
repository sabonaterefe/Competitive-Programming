class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        n = len(flips)
        max_index = 0  
        prefix_aligned_count = 0

        for i in range(n):
            max_index = max(max_index, flips[i])
            if max_index == i + 1:  
                prefix_aligned_count += 1

        return prefix_aligned_count