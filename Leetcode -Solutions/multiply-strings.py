class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            x = int(num1[i])
            carry = 0
            for j in range(n - 1, -1, -1):
                y = int(num2[j])
                product = x * y + carry + result[i + j + 1]
                carry = product // 10
                result[i + j + 1] = product % 10

            result[i] += carry

        result = [str(num) for num in result]
        if result[0] == "0":
            result = result[1:]

        return ''.join(result)
        
        