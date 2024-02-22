class Solution:
   def numRabbits(self, answers: List[int]) -> int:
    maps = Counter(answers)
    res = 0
    for key,value in maps.items():
        res+=(key+1)*ceil(value/(key+1))
    return res