class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def inbound(row, col):
            return ((0 <= row < len(grid)) and (0 <= col < len(grid[0]))  )  

        def land(row, col):
            return inbound(row, col) and grid[row][col] == 1
        def dfs(row, col):
            count = 4
            visited[row][col] = True
            for row_change, col_change in dxn:
                new_row = row + row_change
                new_col = col + col_change

                if land(new_row, new_col):
                    count -= 1
                if inbound(new_row, new_col) and not visited[row][col]:
                    count += dfs(new_row, new_col) 
            return count
        #set the directions and visited
        dxn = [(0,1), (0,-1), (-1,0), (1,0)]
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]:
                    count += dfs(r, c)
        return count

                    
        
