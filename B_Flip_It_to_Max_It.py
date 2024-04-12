t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    s = 0
    pos = 0
    for i in range(len(arr)):
        s += abs(arr[i])
        if arr[i] > 0:
            pos +=1
    i = 0
    cnt = 0
    while i < len(arr):
        if arr[i] < 0:
            cnt +=1
        if arr[i] == 0:
            i +=1
            continue     
        while i < len(arr) and arr[i] <= 0:
            i += 1
        i += 1
    print(s, cnt)