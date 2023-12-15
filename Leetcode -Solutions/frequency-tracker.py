from collections import defaultdict

class FrequencyTracker:
    def __init__(self):
        self.f = defaultdict(int)
        self.g = defaultdict(int)

    def add(self, number):
        self.g[self.f[number]] -= 1
        self.f[number] += 1
        self.g[self.f[number]] += 1

    def deleteOne(self, number):
        if self.f[number]:
            self.g[self.f[number]] -= 1
            self.f[number] -= 1
            self.g[self.f[number]] += 1

    def hasFrequency(self, frequency):
        return self.g[frequency] > 0