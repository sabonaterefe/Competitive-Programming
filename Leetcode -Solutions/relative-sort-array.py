from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = [0] * 1001
        for num in arr1:
            count[num] += 1

        sorted_arr = []
        for num in arr2:
            sorted_arr.extend([num] * count[num])
            count[num] = 0
        for i in range(len(count)):
            if count[i] > 0:
                sorted_arr.extend([i] * count[i])

        return sorted_arr