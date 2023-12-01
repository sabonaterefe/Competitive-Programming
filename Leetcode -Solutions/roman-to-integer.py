class Solution:
    def __init__(self):
        self.roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def romanToInt(self, s):
        result = 0
        prev_value = 0
        
        for c in reversed(s):
            current_value = self.roman_values[c]
            if current_value >= prev_value:
                result += current_value
            else:
                result -= current_value
            prev_value = current_value
            
        return result