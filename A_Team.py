t = int(input())
total = 0
for _ in range(t):
    n = input().split()
    n = list(map(int, n))
    if (n[0] + n[1] + n[2]) >=2:
        total +=1  
print(total)