t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    x = max(a)
    for i in range(n-1):
        x = min(x, abs(a[i] - a[i+1]))

    sorted_array = [abs(a[i] - x) for i in range(n)]
    if sorted_array == sorted(sorted_array):
        print(x)
    else:
        print(-1)