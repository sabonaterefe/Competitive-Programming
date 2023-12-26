class Solution:
    def sortPeople(self, names, heights):
        n = len(heights)
        
        for i in range(n - 1):
            swap  =False
            for j in range(n - i - 1):
                if heights[j] < heights[j + 1]:
                    heights[j], heights[j + 1] = heights[j + 1], heights[j]
                   
                    names[j], names[j + 1] = names[j + 1], names[j]
                    swap = True
            if not swap:
                break
        
        return names