class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def inbound(r, c):
            return ((0 <= r < len(grid)) and (0 <= c < len(grid[0])))

        def land(r,c):
            return grid[r][c] == "1"

        def dfs(r, c):
            visited[r][c] = True

            for row_change, col_change in dxn:
                new_row = r + row_change
                new_col = c + col_change

                if inbound(new_row, new_col) and land(new_row, new_col) and not visited[new_row][new_col]:
                    dfs(new_row, new_col)

        dxn = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and not visited[r][c]:
                    dfs(r, c)
                    ans += 1
        return ans