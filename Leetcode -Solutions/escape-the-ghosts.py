from typing import List

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        xtarget, ytarget = target
        distance_to_target = abs(xtarget) + abs(ytarget)

        for ghost in ghosts:
            xghost, yghost = ghost
            distance_to_ghost = abs(xghost - xtarget) + abs(yghost - ytarget)

            if distance_to_ghost <= distance_to_target:
                return False

        return True