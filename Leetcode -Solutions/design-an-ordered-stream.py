class OrderedStream:
    def __init__(self, n: int):
        self.data = {}
        self.ptr = 0

    def insert(self, id: int, value: str) -> List[str]:
        id -= 1
        self.data[id] = value
        
        result = []
        while self.ptr in self.data:
            result.append(self.data[self.ptr])
            self.ptr += 1
        
        return result
