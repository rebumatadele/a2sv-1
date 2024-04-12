import sys
def i(): return int(sys.stdin.readline().strip())
def l(): return list(map(int, sys.stdin.readline().strip().split()))
def ls(): return sorted(list(map(int, sys.stdin.readline().strip().split())))
def s(): return sys.stdin.readline().strip()
def d(): return [int(digit) for digit in input()]
def c(): return list(sys.stdin.readline().strip())

def grid(row):
    array = []
    for _ in range(row -1):
        array.append(list(map(int, input().split())))
    return array
        
from collections import Counter, defaultdict, deque
from bisect import bisect_right, bisect_left
from math import ceil, sqrt, gcd

edges = i()
g = grid(edges)
print(g)

setA = set()
setB = set()
for val in g:
    # print(val)
    
