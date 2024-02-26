from typing import List
from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deck.sort(reverse=True)
        queue = deque()

        for i in range(n):
            if queue:
                queue.appendleft(queue.pop())

            queue.appendleft(deck[i])

        return list(queue)