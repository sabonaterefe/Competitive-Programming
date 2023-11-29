class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        x_rev= s[::-1]

        
        return x_rev==str(x)
        