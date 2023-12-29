

class Solution:
    def sortSentence(self, s: str) -> str:
        words = [i[-1]+i[:-1] for i in s.split()]
        words.sort()
        ans = ''
        for word in words:
            ans+=word[1:]+" "
        return ans[:-1]

        
 