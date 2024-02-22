class RecentCounter:

    def __init__(self):
       self.queue = deque()


    def ping(self, t: int) -> int:
        self.queue.appendleft(t)
        while self.queue and self.queue[-1] < t - 3000:
            self.queue.pop()
            
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)