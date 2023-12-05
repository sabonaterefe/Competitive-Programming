from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0

        for i in range(len(points) - 1):
            current_point = points[i]
            next_point = points[i + 1]

            dx = abs(next_point[0] - current_point[0])
            dy = abs(next_point[1] - current_point[1])

            total_time += max(dx, dy)

        return total_time