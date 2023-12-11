class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        length = len(arr)
        threshold = length // 4
        
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
            
            if freq[num] > threshold:
                return num
        
        return -1