import sys
def i(): return int(sys.stdin.readline().strip())
def l(): return list(map(int, sys.stdin.readline().strip().split()))
def ls(): return sorted(list(map(int, sys.stdin.readline().strip().split())))
def s(): return sys.stdin.readline().strip()
def d(): return [int(digit) for digit in input()]
def c(): return list(sys.stdin.readline().strip())

from collections import Counter, defaultdict, deque
from bisect import bisect_right, bisect_left
from math import ceil



    
t = i()
for _ in range(t):
    n, h = list(map(int, sys.stdin.readline().strip().split()))
    total = 0
    for _ in range(n):
        w, l = list(map(int, sys.stdin.readline().strip().split()))
        temp = max(w, l)
        total += temp
    if total >= h:
        print("YES")
    else:
        print("NO")