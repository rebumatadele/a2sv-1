class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for r in range(n):
            for c in range(n):
                if r == 0:
                    dp[r][c] = matrix[r][c]
                elif c == 0:
                    dp[r][c] = matrix[r][c] + min(dp[r-1][c], dp[r-1][c+1])
                elif c == n-1:
                    dp[r][c] = matrix[r][c] + min(dp[r-1][c], dp[r-1][c-1])
                else:
                    dp[r][c] = matrix[r][c] + min(dp[r-1][c+1], dp[r-1][c], dp[r-1][c-1])
        return min(dp[-1])