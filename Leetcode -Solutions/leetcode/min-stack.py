class MinStack:
    def __init__(self):
        self.stack = []
        self.min_val = float('inf')

    def push(self, val):
        if val <= self.min_val:
            self.stack.append(self.min_val)
            self.min_val = val
        self.stack.append(val)

    def pop(self):
        if self.stack.pop() == self.min_val:
            self.min_val = self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_val