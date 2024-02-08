class Solution:
    def maxScore(self, s: str) -> int:
        score = s.count('1', 1)
        if s[0] == '0':
            score += 1
        ans = score

        for c in s[1:-1]:
            if c == '0':
                score += 1
            else:
                score -= 1
            ans = max(ans, score)

        return ans