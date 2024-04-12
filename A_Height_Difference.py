for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    arr.sort()
    for i in range(n):
        if arr[i + n] - arr[i] < k:
            print("NO")
            break
    else:
        print("YES")
            