class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

        for i in range(n):
            left_sum = prefix_sum[i]
            right_sum = prefix_sum[n] - prefix_sum[i + 1]

            result[i] = (nums[i] * i - left_sum) + (right_sum - nums[i] * (n - i - 1))

        return result