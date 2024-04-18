class MedianFinder:

    def __init__(self):
       self.minheap = []
       self.maxheap = []

    def addNum(self, num: int) -> None:
        if len(self.minheap) == len(self.maxheap):
            if len(self.minheap) != 0:
                if num <= self.minheap[0]:
                    heappush(self.maxheap, -num)
                else:
                    #swap
                    temp = heappop(self.minheap)
                    heappush(self.maxheap, -temp)
                    heappush(self.minheap, num)
            else:
                heappush(self.maxheap, -num)
        else:
            if -self.maxheap[0] <= num:
                heappush(self.minheap, num)
            else:
                #swap
                    temp = -heappop(self.maxheap)
                    heappush(self.minheap, temp)
                    heappush(self.maxheap, -num)

    def findMedian(self) -> float:
        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] - self.maxheap[0])/2
        return -self.maxheap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()