import sys

def i():
    return int(sys.stdin.readline().strip())

def l(): 
    return list(map(int, sys.stdin.readline().strip().split()))

def s():
    return sys.stdin.readline().strip()
from math import ceil
for _ in range(i()):
    i, e, u = l()
    count = 0
    count += i
    count += e//3
    if e % 3 != 0:
        if (e % 3) + u < 3:
            print(-1)
            continue
    count += ceil((u + e % 3) / 3)
    print(count)
    