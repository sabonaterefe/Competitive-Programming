class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        matrix_set = set()
        for start, end in ranges:
            matrix_set.update(range(start, end+1))
            
        for i in range(left, right+1):
            if i not in matrix_set:
                return False
          
        return True
