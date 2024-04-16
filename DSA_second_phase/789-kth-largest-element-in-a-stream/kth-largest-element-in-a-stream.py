class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.n = nums
        self.n.append(-1e5)
        heapify(self.n)
        for _ in range(len(nums) - k):
            heappop(self.n)

    def add(self, val: int) -> int:
        heappush(self.n, val)
        heappop(self.n)
        return self.n[0]

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)