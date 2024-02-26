class Solution:
    MOD = int(1e9) + 7

    def power(self, x: int, y: int) -> int:
        res = 1
        x = x % self.MOD

        while y > 0:
            if y & 1:
                res = (res * x) % self.MOD
            y = y >> 1
            x = (x * x) % self.MOD

        return res

    def countGoodNumbers(self, n: int) -> int:
        count_of_4s = n // 2
        count_of_5s = n - count_of_4s
        ans = (self.power(4, count_of_4s) * self.power(5, count_of_5s)) % self.MOD
        return ans