from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        combinations = []
        self.backtrack(digits, digit_to_letters, 0, '', combinations)
        
        return combinations
    
    def backtrack(self, digits, digit_to_letters, index, current, combinations):
        if index == len(digits):
            combinations.append(current)
            return
        
        digit = digits[index]
        letters = digit_to_letters[digit]
        
        for letter in letters:
            self.backtrack(digits, digit_to_letters, index + 1, current + letter, combinations)