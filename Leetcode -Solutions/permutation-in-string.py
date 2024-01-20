from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq_s1 = Counter(s1)
        freq_s2 = Counter()

        left = 0
        for right in range(len(s2)):
            freq_s2[s2[right]] += 1

            if right - left + 1 > len(s1):
                freq_s2[s2[left]] -= 1
                if freq_s2[s2[left]] == 0:
                    del freq_s2[s2[left]]
                left += 1

            if freq_s1 == freq_s2:
                return True

        return False