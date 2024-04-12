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
        array.append(list(map(int, input())))
    return array
        
from collections import Counter, defaultdict, deque
from bisect import bisect_right, bisect_left
from math import ceil, sqrt, gcd

n, m = l()
arr = grid(n)
lst = []
for row in range(n):
    set2 = set()
    for col in range(m):
        set2.add(arr[row][col])
    if len(set2) != 1:
        print("NO")
        break
    lst.append(set2.pop())

else:
    for i in range(len(lst) -1):
        if lst[i] == lst[i+1]:
            print("NO")
            break
    else:
        print("YES") 
        
# print(set1)
    