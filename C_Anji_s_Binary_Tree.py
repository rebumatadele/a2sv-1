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


def build(grid):
    # print(grid)
    tree = defaultdict(list)
    for i,val in enumerate(grid):
        tree[i+1] = val
    return tree
    
#accepting test cases   
t = i()
for _ in range(t):
    n = i()
    string = c()
    g =  grid(n)
    tree = build(g)
    print(tree)
    count = float("inf")
    loc = 0
    stack = [1]
    parent = 1
    while stack:
        current = stack.pop()
        if tree[current][0] == tree[current][1] == 0:
            count = min(loc, count)
            loc = 0
        else:
            mov = string[current]
            if mov == "L":
                if tree[current][0]:
                    stack.append(tree[current][0])
                else:
                    loc += 1
                    stack.append(tree[current][1])
            elif mov == "R":
                if tree[current][1]:
                    stack.append(tree[current][1])
                else:
                    loc += 1
                    stack.append(tree[current][0])
            else:
                if parent:
                    stack.append(parent)
                else:
                    stack.append(tree[current][0])
                    stack.append(tree[current][1])
                    loc += 1
                    
        parent = current         
        loc += 1
print(count)
print()
    
    