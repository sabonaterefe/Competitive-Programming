class Solution:
    def flipgame(self, f: List[int], b: List[int]) -> int:
        return min(set(f + b) - set(f[i] for i in range(len(f)) if f[i] == b[i]), default=0)