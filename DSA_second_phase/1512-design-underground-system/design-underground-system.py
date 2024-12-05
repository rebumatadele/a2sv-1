class UndergroundSystem:

    def __init__(self):
        # key = id, value = (startStation, startTime)
        self.checkins = {}
        # key = (startStation, endStation), value lambda: [total times, number or trips]
        self.average = defaultdict(lambda: [0, 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkins[id]
        self.average[(startStation, stationName)][0] += t - startTime
        self.average[(startStation, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if self.average[(startStation, endStation)][0] > 0:
           return self.average[(startStation, endStation)][0] / self.average[(startStation, endStation)][1] 
        return 0.0


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)