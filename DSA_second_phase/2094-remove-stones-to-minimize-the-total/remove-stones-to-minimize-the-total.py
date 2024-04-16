class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-i for i in piles]
        heapify(heap)
        
        for _ in range(k):
            temp = -(heappop(heap))
            print(temp)
            heappush(heap, -(temp - (temp//2)))

        return sum([-i for i in heap])
