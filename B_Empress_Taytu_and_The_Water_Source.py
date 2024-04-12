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

# Helper Function for binary search
def helper(dem, tim, pos, condition):
    total = 0
    test = []
    for i in dem:
        test.append(ceil(i/pos))
    for i in range(len(tim)):
        test[i] *=  tim[i]
        
    if sum(test) <= condition:
        return True

#Binary Search           
def binary(dem, tim, k):
    left = 0
    right = max(dem) + 1
    flag = False
    while left + 1 < right:
        mid = (left + right) // 2
        if helper(dem, tim, mid, k):
            flag = True
            right = mid
        else:
            left = mid
    if flag:
        return right
    else:
        return -1
def solve():
    n, k = l()
    d = l()
    t = l()
    print(binary(d, t, k))
t = i()
for i in range(t):
    solve()