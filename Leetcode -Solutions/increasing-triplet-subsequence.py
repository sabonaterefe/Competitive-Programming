class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        smallest = float('inf')
        second_smallest = float('inf')
        
        for num in nums:
            if num <= smallest:
                smallest = num
            elif num <= second_smallest:
                second_smallest = num
            else:
                return True
        
        return False