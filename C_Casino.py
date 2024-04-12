import sys
def i(): return int(sys.stdin.readline().strip())
def l(): return list(map(int, sys.stdin.readline().strip().split()))
def ls(): return sorted(list(map(int, sys.stdin.readline().strip().split())))
def s(): return sys.stdin.readline().strip()
def d(): return [int(digit) for digit in input()]
def c(): return list(sys.stdin.readline().strip())

t = i()
arr = l()
res = []
for k in arr:
    j = k
    while j % 3 == 0:
        j //= 3
    while j % 2 == 0:
        j //= 2
    if len(res) > 0 and res[-1] != j:
        print("No")
        break
    res.append(j)
else:
    print("Yes")