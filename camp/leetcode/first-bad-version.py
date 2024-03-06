# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n+1
        while left + 1 < right:
            mid = (right+left)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid
        return right