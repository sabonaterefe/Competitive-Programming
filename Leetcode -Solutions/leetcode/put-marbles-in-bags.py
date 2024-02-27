class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        a = sorted(map(int.__add__, weights, weights[1:]))
        return sum(a[len(a)-k+1:]) - sum(a[:k-1])