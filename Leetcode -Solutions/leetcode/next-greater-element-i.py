from typing import List
from collections import deque

class Solution:
    def nextGreaterElement(self, findNums: List[int], nums: List[int]) -> List[int]:
        map = {} 
        stack = []
        
        for num in nums:
            while stack and stack[-1] < num:
                map[stack.pop()] = num
            stack.append(num)
        
        for i in range(len(findNums)):
            findNums[i] = map.get(findNums[i], -1)
        
        return findNums