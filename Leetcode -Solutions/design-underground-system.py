class UndergroundSystem:
    def __init__(self):
        self.checkin = {}
        self.time = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, t0 = self.checkin[id]
        if (startStation, stationName) not in self.time:
            self.time[(startStation, stationName)] = [0, 0]
        self.time[(startStation, stationName)][0] += t - t0
        self.time[(startStation, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, count = self.time[(startStation, endStation)]
        return total_time / count
