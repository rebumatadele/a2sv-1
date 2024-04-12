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

#execution starts
def solve():
    n, k = l()
    if n == k:
        print(0)
    else:
        print((n - (k + 1))*3 + ((k-1) // 2)*3 + (k-1) %2 + 1)
    
t = i()
for i in range(t):
    solve()