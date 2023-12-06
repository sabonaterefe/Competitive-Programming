class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        greater= [i for i in nums if i>pivot]
        smaller = [j for j in nums if j<pivot]
        equal = [k for k in nums if k==pivot]
        result = smaller +equal+greater
        return result
        