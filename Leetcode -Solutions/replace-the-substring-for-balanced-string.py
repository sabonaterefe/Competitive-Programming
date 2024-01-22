class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        target = n // 4

        frequency = {}
        for char in s:
            frequency[char] = frequency.get(char, 0) + 1

        if all(count == target for count in frequency.values()):
            return 0

        left = 0
        minLength = float('inf')

        for right in range(n):
            frequency[s[right]] -= 1

            while all(count <= target for count in frequency.values()):
                minLength = min(minLength, right - left + 1)
                frequency[s[left]] += 1
                left += 1

        return minLength