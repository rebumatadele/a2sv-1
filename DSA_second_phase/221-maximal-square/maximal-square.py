class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        maxx = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r == 0 or c == 0:
                    dp[r][c] = int(matrix[r][c])
                    maxx = max(maxx, dp[r][c])
                else:
                    if matrix[r][c] == "1":
                        dp[r][c] = 1 + min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1])
                        maxx = max(maxx, dp[r][c])
        return maxx ** 2
        
