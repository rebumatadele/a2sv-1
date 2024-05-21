class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        ans = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        for r in range(len(obstacleGrid)):
            for c in range(len(obstacleGrid[0])):
                if r == c == 0:
                    ans[r][c] = 1
                elif r == 0:
                    if obstacleGrid[r][c] == 1:
                        continue
                    ans[r][c] = ans[r][c -1]
                elif c == 0:
                    if obstacleGrid[r][c] == 1:
                        continue
                    ans[r][c] = ans[r - 1][c]
                else:
                    if obstacleGrid[r][c] != 1:
                        ans[r][c] = ans[r][c -1]
                        ans[r][c] += ans[r - 1][c]
                        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        return ans[m - 1][n - 1]
                
