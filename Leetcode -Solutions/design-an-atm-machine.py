class ATM:
    def __init__(self):
        self.banknotes = [0, 0, 0, 0, 0]

    def deposit(self, banknotesCount):
        for i in range(len(banknotesCount)):
            self.banknotes[i] += banknotesCount[i]

    def withdraw(self, amount):
        withdrawn = [0, 0, 0, 0, 0]
        remaining = amount

        for i in range(4, -1, -1):
            banknote = [20, 50, 100, 200, 500][i]
            count = min(remaining // banknote, self.banknotes[i])
            remaining -= count * banknote
            withdrawn[i] = count

        if remaining == 0:
            for i in range(4, -1, -1):
                self.banknotes[i] -= withdrawn[i]
            return withdrawn

        return [-1]