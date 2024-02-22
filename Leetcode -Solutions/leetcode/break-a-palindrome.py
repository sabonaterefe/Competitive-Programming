class Solution:
    def breakPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1: return ""
        for i in range(0, n//2): 
            if s[i] != "a": return s[0:i]+"a"+s[i+1:]
        return  s[0:-1] +"b"