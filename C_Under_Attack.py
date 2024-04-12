from collections import defaultdict
t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    rows = arr[0]
    cols = arr[1]
    array = []
    dic = defaultdict(list)
    for i in range(rows):
        a = list(map(int, input().split()))
        array.append(a)
    # print(array)
    lst = defaultdict(int)
    lst2 = defaultdict(int)
    total = 0
    for r in range(rows):
        for c in range(cols):
            lst[r+c] +=array[r][c]
            lst2[r-c] +=array[r][c]
    for r in range(rows):
        for c in range(cols):
            total = max(total, (lst[r + c] + lst2[r - c]) -array[r][c])
    print(total)
    
            