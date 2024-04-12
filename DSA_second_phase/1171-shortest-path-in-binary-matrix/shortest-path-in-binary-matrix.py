class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        dxn = [(1,0), (-1,0), (0,1), (0,-1), (1, 1), (-1,-1), (1,-1), (-1,1)]

        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 1 if not grid[0][0] else -1
        
        if grid[0][0] or grid[m - 1][n - 1]:
            return -1

        def inbound(r, c):
            return (0<= r< m and 0<= c < n)

        que = deque([(0,0,1)])
        visited = set([(0,0)])
        
        while que:
            r, c, path = que.popleft()
            
            for cr, cc in dxn:
                new_row = cr + r
                new_col = cc + c

                if new_row == m - 1 and new_col == n - 1:
                    return path + 1

                if inbound(new_row, new_col) and grid[new_row][new_col] == 0:
                    if (new_row, new_col) not in visited:
                        que.append((new_row, new_col, path + 1))
                        visited.add((new_row, new_col) )
        return -1
