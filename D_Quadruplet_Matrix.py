from collections import defaultdict
t = int(input())
for _ in range(t):
    size = int(input())
    array = []
    total = 0
    for i in range(size):
        a = list(map(int, input()))
        array.append(a)
    for r in range(size):
       
        for c in range(size):
            lst2 = []
            lst2.append(array[r][c])
            lst2.append(array[c][size-1-r])
            lst2.append(array[size-1-r][size-1-c])
            lst2.append(array[size-1-c][r])
            total+=min(lst2.count(0), lst2.count(1))
     
    print(int(total/4))     
