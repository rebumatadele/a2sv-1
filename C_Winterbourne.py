t = int(input())
for _ in range(t):
    p , c = map(int, input().split())
    array = list(map(int, input().split()))
    array.sort(reverse = True)
    total = 0
    for i in range(p):
        if i == 0:
            total +=array[i] *2
            continue
        elif i == p-1:
            break
        total += array[i]
    if total + p > c:
        print("NO")
    else:
        print("YES")