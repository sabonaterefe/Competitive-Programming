class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        operators = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(int(x) / y)
        }

        operation = None

        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                r, l = stack.pop(), stack.pop()
                operation = operators[t]
                stack.append(operation(l, r))

        return stack.pop()