t = int(input())
for _ in range(t):
    size = int(input())
    lst = list(map(int, input().split()))
    res = []
    cnt1 = 0
    for i, val in enumerate(lst):
        if val == 0:
            continue
        else:
            cnt1 = i
            break
    cnt2 = 0
    for i in range(len(lst)-1, -1, -1):
        if lst[i] == 0:
            continue
        else:
            cnt2 = i
            break
    res = lst[cnt1 : cnt2+1] 
    print(res.count(0))