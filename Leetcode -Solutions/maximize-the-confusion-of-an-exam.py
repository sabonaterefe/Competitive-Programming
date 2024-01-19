class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        maxConsecutive = 0
        maxCount = 0
        counts = {'T': 0, 'F': 0}  

        left = right = 0

        while right < n:
            counts[answerKey[right]] += 1
            maxCount = max(maxCount, counts[answerKey[right]])
            if (right - left + 1) - maxCount > k:
                counts[answerKey[left]] -= 1
                left += 1

            maxConsecutive = max(maxConsecutive, right - left + 1)
            right += 1

        return maxConsecutive