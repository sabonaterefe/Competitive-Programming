from typing import List

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        if len(set(cards)) == len(cards):
            return -1
        
        dic = {}
        ma = float('inf')
        
        for i, card in enumerate(cards):
            if card in dic:
                distance = i - dic[card]
                if distance < ma:
                    ma = distance
            dic[card] = i
        
        return ma + 1