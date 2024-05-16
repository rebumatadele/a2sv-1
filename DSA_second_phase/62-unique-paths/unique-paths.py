class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0 for _ in range(n)] for _ in range(m)]
        print(memo)
        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0:
                    memo[r][c] = 1
                elif r == 0: 
                    memo[r][c] = memo[r][c-1]
                elif c == 0:
                    memo[r][c] = memo[r-1][c]
                else:
                    memo[r][c] = memo[r][c-1] + memo[r-1][c]
        return memo[m-1][n-1]

