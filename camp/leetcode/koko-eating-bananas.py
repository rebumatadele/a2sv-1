class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper(pos):
            total = 0
            hi = 0
            for i in piles:
                hi += ceil(i/pos)
            if hi <= h:
                return True
        left = 0
        right = max(piles)
        while left + 1 < right:
            mid = (left + right) // 2
            if helper(mid):
                right = mid
            else:
                left = mid
        return right