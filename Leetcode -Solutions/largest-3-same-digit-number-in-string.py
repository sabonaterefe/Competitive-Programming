class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_good = ""
        for i in range(len(num)-2):
            substring = num[i:i+3]
            unique_digit = len(set(substring))==1
            if unique_digit and substring>max_good:
                max_good = substring
        return max_good
        
        