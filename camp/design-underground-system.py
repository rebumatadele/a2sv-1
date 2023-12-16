class UndergroundSystem:

    def __init__(self):
        self.checkin_dict = defaultdict(tuple)
        self.checkout_dict = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin_dict[id] = (t, stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        starttime,startstation=self.checkin_dict[id]
        total=t-starttime
        self.checkout_dict[(startstation,stationName)].append(total)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
                return sum(self.checkout_dict[(startStation,endStation)])/len(self.checkout_dict[(startStation,endStation)])

        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
# 