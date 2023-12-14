class Solution:
    def minimizedStringLength(self, s: str) -> int:
        v = [False] * 26
        ans = 0
        for i in s:
            if not v[ord(i) - ord('a')]:
                ans += 1
                v[ord(i) - ord('a')] = True
        return ans