from functools import reduce
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

def factor(n):
    i = 1
    while i * i <= n:
        if n % i == 0:
            if i % 2 == 1 and i != 1:
                return True
            if i != n // i and (n // i) % 2 == 1:
                return True
        i += 2
    return False

#execution starts here
def solve():
    n = int(sys.stdin.readline().strip())
    if n % 2 == 0:
        while n > 0 and n % 2 == 0:
            n = n //2
        if n != 1 and n % 2 == 1:
            print("YES")
            return
    else:
        if factor(n):
            print("YES")
            return
    print("NO") 
    
#accepting test cases   
t = i()
for i in range(t):
    solve()