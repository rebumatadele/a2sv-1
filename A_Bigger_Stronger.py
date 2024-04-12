t = int(input())
for _ in range(t):
    size = int(input())
    array = list(map(int, input().split()))
    arr = set(array)
    if len(arr)<len(array):
        print("NO")
    else:
        print("YES")