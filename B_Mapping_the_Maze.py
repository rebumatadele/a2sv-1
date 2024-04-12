import sys
def i(): return int(sys.stdin.readline().strip())
def l(): return list(map(int, sys.stdin.readline().strip().split()))
def ls(): return sorted(list(map(int, sys.stdin.readline().strip().split())))
def s(): return sys.stdin.readline().strip()
def d(): return [int(digit) for digit in input()]
def c(): return list(sys.stdin.readline().strip())

def grid(col):
    array = []
    for _ in range(col):
        a = list(map(int, input().split()))
        array.append(a)
    return array
        
from collections import Counter, defaultdict, deque
from bisect import bisect_right, bisect_left
from math import ceil, sqrt, gcd

def build(graph):
    gra = defaultdict(list)
    for val in graph:
        gra[val[0]].append(val[1])
    return gra
    
    
n, m = l()
ar = grid(m)
graph = build(ar)

# print(graph)

count = defaultdict(int)
for key, val in graph.items():
    count[key] += len(val)
    for i in val:
        count[i] += 1
# print(count)
start = min(count.keys())

myset = set()
maxx = 1
for key, val in count.items():
    myset.add(val)
    if val > count[maxx]:
        maxx = key

bus = 0           
for val in count.values():
    if val == 1:
        bus += 1      
        
if len(myset) == 2 and bus == 2:
    print("bus topology")
        
elif count[start] == 2 and len(myset) == 1:
    print("ring topology")
    
elif bus == n-1 and count[maxx] == n - 1:
        print("star topology")
else:
    print("unknown topology")
