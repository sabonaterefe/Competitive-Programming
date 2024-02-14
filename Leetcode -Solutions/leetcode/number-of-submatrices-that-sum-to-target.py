class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        count = 0

        for c1 in range(n):
            prefix_sum = [0] * m
            for c2 in range(c1, n):
                prefix_sum_map = {0: 1}
                current_sum = 0

                for row in range(m):
                    prefix_sum[row] += matrix[row][c2]
                    current_sum += prefix_sum[row]

                    count += prefix_sum_map.get(current_sum - target, 0)
                    prefix_sum_map[current_sum] = prefix_sum_map.get(current_sum, 0) + 1

        return count