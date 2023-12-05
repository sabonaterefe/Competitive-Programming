from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(indices)
        shuffled_string = [''] * n

        for i in range(n):
            shuffled_string[indices[i]] = s[i]

        return ''.join(shuffled_string)