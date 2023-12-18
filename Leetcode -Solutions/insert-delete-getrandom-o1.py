import random

class RandomizedSet:
    def __init__(self):
        self.set_array = []
        self.set_dict = {}

    def insert(self, val: int) -> bool:
        if val in self.set_dict:
            return False

        self.set_array.append(val)
        self.set_dict[val] = len(self.set_array) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.set_dict:
            return False

        index = self.set_dict[val]
        last_val = self.set_array[-1]

        self.set_array[index] = last_val
        self.set_dict[last_val] = index

        self.set_array.pop()
        del self.set_dict[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.set_array)