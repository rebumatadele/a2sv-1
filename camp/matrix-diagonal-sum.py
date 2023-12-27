class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        lst = []
        lst1 = []
        for r in range(rows):
            for c in range(cols):
                if r == c:
                    lst.append(mat[r][c])
                elif r + c == cols-1:
                    lst1.append(mat[r][c])
        return (sum(lst + lst1))