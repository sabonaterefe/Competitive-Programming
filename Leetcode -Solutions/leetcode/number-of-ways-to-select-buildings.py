class Solution:
    def numberOfWays(self, s: str) -> int:
        ans = 0
        ones = 0
        zeros = 0
        options_for_zeros = 0
        options_for_ones = 0
        for x in s:
            if x == '1':
                ans += options_for_ones
                options_for_zeros += zeros
                ones += 1
            else:
                ans += options_for_zeros
                options_for_ones += ones
                zeros += 1
        return ans