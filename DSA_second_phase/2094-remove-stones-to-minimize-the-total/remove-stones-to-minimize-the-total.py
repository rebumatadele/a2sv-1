class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        for val in piles:
            heappush(heap, -val)

        for _ in range(k):
            temp = -(heappop(heap))
            print(temp)
            heappush(heap, -(temp - (temp//2)))
        ret = 0
        for i in heap:
            ret += -i
        return ret