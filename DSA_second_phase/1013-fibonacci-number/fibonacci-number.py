class Solution:
    def fib(self, n: int) -> int:
        def helper(i):
            if i == 0 or i == 1:
                return i
            elif i not in memo:
                memo[i] = helper(i - 1) + helper(i-2)
            return memo[i]
        memo = defaultdict(int)
        return helper(n)

        