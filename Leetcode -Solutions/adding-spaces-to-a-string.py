class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        lastIdx = 0
        for i in spaces:
            res += s[lastIdx:i]
            res += " "
            lastIdx = i
        res += s[lastIdx:]
        return res