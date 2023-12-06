class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n = len(nums)//2
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i+n])
        return result

        