class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        def inbound(r, c):
            return (0<= r< len(grid) and 0<= c < len(grid[0]))

        fresh = 0
        que = deque()
        directions = [(1,0), (-1,0), (0, 1), (0, -1)]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    que.append((r,c))
        time = 0
        while que and fresh > 0:
            for _ in range(len(que)):
                r, c = que.popleft()
                for cr, cc in directions:
                    new_row = r + cr
                    new_col = c + cc

                    if inbound(new_row, new_col) and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        que.append((new_row, new_col))
                        fresh -= 1
            time += 1
        if fresh == 0:
            return time 
        else:
            return -1



                