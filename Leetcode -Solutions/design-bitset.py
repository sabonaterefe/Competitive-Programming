class Bitset:
    def __init__(self, size: int):
        self.bit = [False] * size
        self.bitinv = [True] * size
        self.ones = 0
        self.zeros = size
        self.size = size

    def fix(self, idx: int) -> None:
        if not self.bit[idx]:
            self.zeros -= 1
            self.ones += 1
        self.bit[idx] = True
        self.bitinv[idx] = False

    def unfix(self, idx: int) -> None:
        if self.bit[idx]:
            self.zeros += 1
            self.ones -= 1
        self.bit[idx] = False
        self.bitinv[idx] = True

    def flip(self) -> None:
        self.ones, self.zeros = self.zeros, self.ones
        self.bit, self.bitinv = self.bitinv, self.bit

    def all(self) -> bool:
        return self.ones == self.size

    def one(self) -> bool:
        return self.ones > 0

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        return ''.join(['1' if bit else '0' for bit in self.bit])