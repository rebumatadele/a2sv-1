class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        def inbound(r, c):
            return ((0 <= r < len(grid)) and (0 <= c < len(grid[0])))
        
        def dfs(row, col):
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return True
            visited.add((row, col))
            current = grid[row][col] -1
            
            for row_change, col_change in dxn[current]:
                new_row = row + row_change
                new_col = col + col_change
                
                if inbound(new_row, new_col) and (new_row, new_col) not in visited and (-row_change, -col_change) in dxn[grid[new_row][new_col] -1]:
                    found = dfs(new_row, new_col)
                    if found:
                        return True
            return False

        #set up the direction and the visited
        dxn = [[(0,1), (0,-1)], 
                [(1,0), (-1,0)], 
                [(0,-1), (1,0)], 
                [(0,1), (1,0)],  
                [(0,-1), (-1,0)], 
                [(0,1), (-1,0)]
                ]
        visited = set()
        return dfs(0, 0)