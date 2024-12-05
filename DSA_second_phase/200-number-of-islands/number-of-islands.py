class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        1. Use a set to keep the vissisted positions
        2. We will use a queue since we are using a BFS
        """ 
        islands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
        def inbound(r, c):
            return (0<= r < rows) and (0 <= c < cols)
        def dfs(r, c):
            visited.add((r, c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if inbound(nr, nc) and grid[nr][nc] == "1" and (nr, nc) not in visited:
                    dfs(nr, nc)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    dfs(r, c)
        return islands
