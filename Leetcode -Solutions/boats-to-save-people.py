class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boatCount = 0
        people.sort()
        
        left = 0
        right = len(people) - 1
        
        while left <= right:
            totalWeight = people[left] + people[right]
            if totalWeight <= limit:
                boatCount += 1
                left += 1
                right -= 1
            else:
                boatCount += 1
                right -= 1
        
        return boatCount