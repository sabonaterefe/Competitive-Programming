class Solution:
    def pancakeSort(self, A):
        res = []
        
        for x in range(len(A), 1, -1):
            max_index = self.find_max_index(A[:x])
            
            if max_index != x - 1:
                self.flip(A, max_index + 1)
                res.append(max_index + 1)
                self.flip(A, x)
                res.append(x)
        
        return res
    
    def find_max_index(self, arr):
        max_val = float('-inf')
        max_index = -1
        
        for i, val in enumerate(arr):
            if val > max_val:
                max_val = val
                max_index = i
        
        return max_index
    
    def flip(self, arr, k):
        i = 0
        while i < k // 2:
            arr[i], arr[k - i - 1] = arr[k - i - 1], arr[i]
            i += 1