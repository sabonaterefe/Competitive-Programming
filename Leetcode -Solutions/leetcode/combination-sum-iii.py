class Solution:
    def combinationSum3(self, k, n):
        def backtrack(start, target, combination):
            if target == 0 and len(combination) == k:
                result.append(combination[:])
                return
            if target < 0 or len(combination) > k:
                return
            for i in range(start, 10):
                combination.append(i)
                backtrack(i + 1, target - i, combination)
                combination.pop()

        result = []
        backtrack(1, n, [])
        return result