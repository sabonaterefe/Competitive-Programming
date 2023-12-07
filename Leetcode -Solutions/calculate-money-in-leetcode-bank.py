class Solution:
    def totalMoney(self, n: int) -> int:
        monday= 0
        total_money = 0
        for day in range(n):
            if day%7==0:
                monday+=1
            total_money+=monday+(day%7)
        return total_money