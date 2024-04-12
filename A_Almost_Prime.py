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

def prime(n):
    is_prime:list[bool] = [True for _ in range(n + 1)]
    is_prime[0] = is_prime[1] = False
    d = 2
    while d*d <= n:
        if is_prime[d]:
            i = d * d
            while i <= n:
                is_prime[i] = False
                i += d
        d += 1          
    return is_prime

t = i()
gcount = 0
for i in range(2, t+1):
    count = 0
    for j, val in enumerate(prime(i)):
        if val and i % j == 0:
            count += 1
    if count == 2:
        gcount += 1              
print(gcount)