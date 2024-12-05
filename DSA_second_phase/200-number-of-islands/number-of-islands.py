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
        def bfs(r, c):
            que = deque()
            visited.add((r, c))
            que.append((r,c))

            while que:
                row, col = que.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if inbound(r, c) and grid[r][c] == "1" and (r, c) not in visited:
                        que.append((r, c))
                        visited.add((r, c))



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    bfs(r, c)
        return islands
