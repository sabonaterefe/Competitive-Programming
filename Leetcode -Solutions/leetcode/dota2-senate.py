from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()

        for i in range(len(senate)):
            if senate[i] == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            radiant_senator = radiant.popleft()
            dire_senator = dire.popleft()

            if radiant_senator < dire_senator:
                radiant.append(radiant_senator + len(senate))
            else:
                dire.append(dire_senator + len(senate))

        return "Radiant" if len(radiant) > 0 else "Dire"