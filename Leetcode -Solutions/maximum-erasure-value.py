class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        unique_nums = set()
        left = right = 0
        max_score = 0
        current_score = 0

        while right < n:
            if nums[right] not in unique_nums:
                unique_nums.add(nums[right])
                current_score += nums[right]
                max_score = max(max_score, current_score)
                right += 1
            else:
                unique_nums.remove(nums[left])
                current_score -= nums[left]
                left += 1

        return max_score