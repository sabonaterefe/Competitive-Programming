class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counts = [0] * 101  
        result = []
      
        for num in nums:
            counts[num] += 1
        for i in range(1, len(counts)):
            counts[i] += counts[i-1]
        for num in nums:
            if num == 0:
                result.append(0)
            else:
                result.append(counts[num-1])
        
        return result