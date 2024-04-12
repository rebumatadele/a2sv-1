t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    num = set()
    for i in range(len(arr)):
        if arr[i] in num:
            continue
        elif arr.count(arr[i]) >1:
            num.add
            (arr[i])
        elif arr.count(arr[i]) ==1:
            print(i+1)
            break
