class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        i,j = click[0],click[1]
        
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board
        
        m,n = len(board),len(board[0])
        st = [(i,j)]
        dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        
        while st:
            x,y = st.pop()
            if board[x][y] == 'E':
                cnt = 0
                for dx,dy in dirs:
                    new_x, new_y = x+dx, y+dy
                    if 0<=new_x<m and 0<=new_y<n and board[new_x][new_y] == 'M':
                        cnt += 1
                if cnt == 0:
                    board[x][y] = 'B'
                    for dx,dy in dirs:
                        new_x, new_y = x+dx, y+dy
                        if 0<=new_x<m and 0<=new_y<n:
                            st.append((new_x,new_y))
                else:
                    board[x][y] = str(cnt)
        return board