class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        reversed_chunks = [s[i:i+k][::-1] + s[i+k:i+2*k] for i in range(0, n, 2*k)]
        return ''.join(reversed_chunks)