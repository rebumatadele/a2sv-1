class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s = []
        for i in stones:
            s.append(-i)
        heapify(s)
        print(s)
        while len(s) > 1:
            x, y = nsmallest(2, s)
            x = -x
            y = -y
            heappop(s)
            heappop(s)
            if x != y:
                heappush(s, -(max(x,y) - min(x,y)))
        if len(s) == 0:
            return 0
        return(-s[0])