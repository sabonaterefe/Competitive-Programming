class Solution:
    def totalFruit(self, fruits):
        res = 0
        start = 0
        end = 0
        fruit1 = None
        fruit2 = None
        fruit1_count = 0
        fruit2_count = 0
        
        while end < len(fruits):
            fruit = fruits[end]
            
            if fruit == fruit1:
                fruit1_count += 1
            elif fruit == fruit2:
                fruit2_count += 1
            elif fruit1 is None:
                fruit1 = fruit
                fruit1_count = 1
            elif fruit2 is None:
                fruit2 = fruit
                fruit2_count = 1
            else:
                res = max(res, end - start)
                while fruit1_count > 0 and fruit2_count > 0:
                    start_fruit = fruits[start]
                    if start_fruit == fruit1:
                        fruit1_count -= 1
                    elif start_fruit == fruit2:
                        fruit2_count -= 1
                    start += 1
                
                if fruit1_count == 0:
                    fruit1 = fruit
                    fruit1_count = 1
                else:
                    fruit2 = fruit
                    fruit2_count = 1
            
            res = max(res, end - start + 1)
            end += 1
        
        return res