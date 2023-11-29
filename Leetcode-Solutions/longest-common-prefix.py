class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        v = sorted(strs)
        beg = v[0]
        last = v[-1]
        for i in range (min(len(beg), len(last))):
            if beg[i]!=last[i]:
                return prefix
            prefix+=beg[i]
        return prefix 
        