from typing import List

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def getNextIndex(i: int) -> int:
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            slow = i
            fast = getNextIndex(i)

            while nums[i] * nums[fast] > 0 and nums[i] * nums[getNextIndex(fast)] > 0:
                if slow == fast:
                    if slow == getNextIndex(slow):
                        break
                    return True

                slow = getNextIndex(slow)
                fast = getNextIndex(getNextIndex(fast))

            slow = i
            while nums[i] * nums[slow] > 0:
                next_slow = getNextIndex(slow)
                nums[slow] = 0
                slow = next_slow

        return False