from typing import List

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        ans = 0
        n = len(skill)

        if n == 3:
            return skill[0] * skill[1]

        skill.sort()
        i = n // 2 - 1
        j = n // 2
        total_skill = skill[i] + skill[j]

        while i >= 0 and j < n:
            tmp = skill[i] + skill[j]

            if tmp == total_skill:
                ans += skill[i] * skill[j]
            else:
                ans = 0
                break

            i -= 1
            j += 1

        if ans == 0:
            return -1

        return ans