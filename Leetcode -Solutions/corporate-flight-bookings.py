from typing import List

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix_sum = [0] * n

        for booking in bookings:
            start, end, seats = booking
            prefix_sum[start - 1] += seats
            if end < n:
                prefix_sum[end] -= seats

        for i in range(1, n):
            prefix_sum[i] += prefix_sum[i - 1]

        return prefix_sum