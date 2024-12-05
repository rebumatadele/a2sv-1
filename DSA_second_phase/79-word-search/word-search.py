class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def inbound(r, c):
            return (0 <= r < len(board)) and 0 <= c < len(board[0])
        def backtrack(r, c, k):
            if k == len(word):
                return True
            if not inbound(r, c) or board[r][c] != word[k]:
                return False
            
            temp = board[r][c]
            board[r][c] = ""

            if backtrack(r+1, c, k+1) or backtrack(r-1, c, k+1) or backtrack(r, c+1, k+1) or backtrack(r, c-1, k+1):
                return True
            board[r][c] = temp
            return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtrack(r, c, 0):
                    return True
        return False