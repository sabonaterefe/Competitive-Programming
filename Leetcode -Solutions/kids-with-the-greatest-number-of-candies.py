from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        result = [candy_count + extraCandies >= max_candies for candy_count in candies]
        return result