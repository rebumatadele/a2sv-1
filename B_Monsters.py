t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    health = list(map(int, input().split()))
    res = []
    for i in range(len(health)):
        res.append((i+1, health[i] % k)) 
    res = sorted(res, key=lambda x: (x[1], x[0]))

    for i in range(len(res)):
        print(res[i][0], end=" ")
    print()