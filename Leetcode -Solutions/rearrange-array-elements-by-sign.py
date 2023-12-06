class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negative =[i for i in nums if i<0]
        positive=[j for j in nums if j>0]
        n = len(nums)//2
        result = []
        for i in range(n):
            result.append(positive[i])
            result.append(negative[i])
        return result
