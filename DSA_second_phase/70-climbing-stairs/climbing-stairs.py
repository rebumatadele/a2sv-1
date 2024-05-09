class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def helper(i):
            if i == 1 or i == 2:
                return i
            return helper(i-1) + helper(i-2)  
        return helper(n)