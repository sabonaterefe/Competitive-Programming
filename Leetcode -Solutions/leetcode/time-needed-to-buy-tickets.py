from typing import List
from collections import deque

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        queue = deque()
        time = 0

        for i in range(n):
            queue.append((i, tickets[i]))

        while queue:
            person = queue.popleft()
            position, ticket_count = person

            ticket_count -= 1

            if ticket_count > 0:
                queue.append((position, ticket_count))

            time += 1

            if position == k and ticket_count == 0:
                return time

        return -1