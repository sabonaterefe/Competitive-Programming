class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = ['(', '[', '{']
        closing = [')', ']', '}']
        mapping = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in opening:
                stack.append(char)
            elif char in closing:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
        
        return len(stack) == 0