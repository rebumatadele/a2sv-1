class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        grid = [[0 for _ in range(n)] for _ in range(m)] 
        
        for [i,j] in guards:
            grid[i][j] = 1   
        for [i,j] in walls:
            grid[i][j] = -1
        
        def dfs(i,j,di):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j] == 1 or grid[i][j] == -1:
                return
            else:
                grid[i][j] = 2
            i = i + lst[di]
            j = j + lst[di+1]
            dfs(i,j,di)
        
        lst = [1,0,-1,0,1]
        for [i,j] in guards:
            for idx in range(4):  
                k = i + lst[idx]
                l = j + lst[idx+1]
                dfs(k,l,idx)
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    count +=1
        return count