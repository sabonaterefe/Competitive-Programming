class Solution:
    def isAlienSorted(self, words, order):
        alien_dict = {char: i for i, char in enumerate(order)}

        for i in range(1, len(words)):
            prev_word = words[i - 1]
            curr_word = words[i]
            
        
            for j in range(len(prev_word)):
           
                if j >= len(curr_word) or alien_dict[prev_word[j]] > alien_dict[curr_word[j]]:
                    return False
                elif alien_dict[prev_word[j]] < alien_dict[curr_word[j]]:
                    break
        
        return True