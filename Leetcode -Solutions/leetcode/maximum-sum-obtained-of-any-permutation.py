class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        count = [0] * (n + 1)
        for start, end in requests:
            count[start] += 1
            count[end + 1] -= 1
        for i in range(1, n + 1):
            count[i] += count[i - 1]

        count.pop() 

    
        nums.sort(reverse=True)
        count.sort(reverse=True)

        total_sum = sum(num * freq for num, freq in zip(nums, count))

        return total_sum % MOD