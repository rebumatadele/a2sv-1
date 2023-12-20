class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        from collections import defaultdict
        size = (len(mat) + len(mat[0])) - 1
        out = defaultdict(list)
        lst = []

        for r in range(len(mat)):
            for c in range(len(mat[0])):
                out[r+c].append(mat[r][c])
        print(out)

        for i,value in out.items():
            if i == 0 or i%2==0:
                value.reverse()
            lst.extend(value)
        return(lst)
        


        


