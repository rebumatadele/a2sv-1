from collections import defaultdict
n = int(input())
mat = []
for i in range(n):
        a = list(map(int, input().split()))
        mat.append(a)

rows = n
cols = n
total = 0
dic = defaultdict(list)
for r in range(rows):
    for c in range(cols):
        if r == c:
            total +=mat[r][c]
        elif r + c == n-1:
            total +=mat[r][c]
        elif (n-1)/2 == c:
            total +=mat[r][c]
        elif (n-1) /2 ==r:
            total +=mat[r][c]
print(total)