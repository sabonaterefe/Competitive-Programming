class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []
        ret = [0] * len(temperatures)
        max_index = len(temperatures) - 1
        
        for i in range(len(temperatures) - 1, -1, -1):
            if temperatures[i] >= temperatures[max_index]:
                max_index = i
            else:
                while stack and temperatures[i] >= temperatures[stack[-1]]:
                    stack.pop()
                if stack:
                    ret[i] = stack[-1] - i
            stack.append(i)
        
        return ret