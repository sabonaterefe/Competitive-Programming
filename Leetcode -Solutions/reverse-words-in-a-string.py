class Solution:
    def reverseWords(self, s: str) -> str:
        splitted= list(s.split())
        reversed_string= splitted[::-1]
        return " ".join(reversed_string).strip()
        