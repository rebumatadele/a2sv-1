class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        ans = w
        heap = []
        for i in range(len(capital)):
            heappush(heap, (capital[i], profits[i]))

        available = []
        # k += 1
        while k:
            while heap and heap[0][0] <= w:
                heappush(available, -heappop(heap)[1])

            if available:
                current = -heappop(available)
                ans += current
                w += current
                k -= 1
            else:
                break

            
        return ans