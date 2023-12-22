class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strin_list = [str(digit) for digit in digits]  
        inter = int("".join(strin_list))
        inter += 1
        inter_stringfy = str(inter)
        inter_list = [int(digit) for digit in inter_stringfy]  
        return inter_list