import sys
def i(): return int(sys.stdin.readline().strip())
def l(): return list(map(int, sys.stdin.readline().strip().split()))
def ls(): return sorted(list(map(int, sys.stdin.readline().strip().split())))
def s(): return sys.stdin.readline().strip()
def d(): return [int(digit) for digit in input()]
def c(): return list(sys.stdin.readline().strip())

from collections import Counter, defaultdict, deque
from bisect import bisect_right, bisect_left
from math import ceil, sqrt, gcd


#execution starts here
def solve():
    c = list(sys.stdin.readline().strip())
    # print(c)
    s = set(c)
    if len(s) == 1:
        print(-1)
    else:
        print(len(c) - 1)
#accepting test cases   
t = i()
for i in range(t):
    solve()