from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timestamps = [0] * 1001  # Assuming maximum timestamp is 1000

        for num, start, end in trips:
            timestamps[start] += num
            timestamps[end] -= num

        used_capacity = 0
        for passenger_change in timestamps:
            used_capacity += passenger_change
            if used_capacity > capacity:
                return False

        return True