from collections import deque

class Solution:
    def shortestSubarray(self, A, K):
        n = len(A)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + A[i]
        
        min_length = float('inf')
        queue = deque()
        
        for i in range(n + 1):
            while queue and prefix_sum[i] - prefix_sum[queue[0][0]] >= K:
                min_length = min(min_length, i - queue[0][0])
                queue.popleft()
            
            while queue and prefix_sum[i] <= prefix_sum[queue[-1][0]]:
                queue.pop()
            
            queue.append((i, prefix_sum[i]))
        
        return min_length if min_length != float('inf') else -1