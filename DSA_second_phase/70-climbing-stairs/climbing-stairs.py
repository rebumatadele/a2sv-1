class Solution:
    def climbStairs(self, n: int) -> int:
        def helper(i):
            if i == 1 or i == 2:
                return i
            if i not in memo:
                memo[i] = helper(i-1) + helper(i-2)
            return memo[i]
            
        memo = defaultdict(int)
        return helper(n)