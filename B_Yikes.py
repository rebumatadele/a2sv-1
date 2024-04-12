import sys

def i():
    return int(sys.stdin.readline().strip())

def l():
    return list(map(int, sys.stdin.readline().strip().split()))

def s():
    return sys.stdin.readline().strip()
from bisect import bisect_left
n = i()
lst = l()
juicy = i()
label = l()

query = []
total = 0
query.append(0)
for i in lst:
    query.append(total + i) 
    total += i
# print(query)
for i in label:
    print(bisect_left(query, i)) 
    
    