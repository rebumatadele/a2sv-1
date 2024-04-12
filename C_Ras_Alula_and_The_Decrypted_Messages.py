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

def solve():
    n, m = l()
    s, w = c(), c()
    i, j = 0, (m - 1)
    ans = 0
    sans = 0
    for k in range(m):
        ans += ord(w[k] )
        sans += ord(s[k])        
    if ans == sans:
        print("YES")
        return
    j += 1
    while j < n:
        sans -= ord(s[i])  
        sans += ord(s[j]) 
        i += 1
        j += 1
        if sans == ans:
            print("YES")
            break
    else:
        print("NO")   
t = i()
for i in range(t):
    solve()