class Solution:
    def average(self, salary):
        if len(salary) <= 2:
            return 0

        total = sum(salary)
        minimum = min(salary)
        maximum = max(salary)
        num_employees = len(salary) - 2
        average = (total - minimum - maximum) / num_employees

        return average