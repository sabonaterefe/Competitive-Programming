from typing import List

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()  
        n = len(piles) // 3
        coins = sum(piles[-2*n::2])  
        return coins