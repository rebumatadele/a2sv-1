t = int(input())
for _ in range(t):
    sub = input()
    total ="Yes" * ((50//3) + 2)
    if sub in total:
        print("YES")
    else:
        print("NO")        
