class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #find the index of x in the array
        heap = []
        for i, val in enumerate(arr):
            heappush(heap, (-(abs(val - x)), -val))
            if len(heap) > k:
                heappop(heap)
        print(heap)
        ans = []
        for val in heap:
            ans.append(-val[1])
        ans.sort()

        return ans


