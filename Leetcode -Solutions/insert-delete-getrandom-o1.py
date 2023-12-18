import random
class RandomizedSet:

    def __init__(self):
        self.set_list = []
        

    def insert(self, val: int) -> bool:
        if val not in self.set_list:
            self.set_list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.set_list:
            return False
        self.set_list.remove(val)
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.set_list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()