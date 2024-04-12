import sys
def i(): return int(sys.stdin.readline().strip())
def l(): return list(map(int, sys.stdin.readline().strip().split()))
def ls(): return sorted(list(map(int, sys.stdin.readline().strip().split())))
def s(): return sys.stdin.readline().strip()
def d(): return [int(digit) for digit in input()]
def c(): return list(sys.stdin.readline().strip())

from collections import Counter, defaultdict, deque
from math import gcd
def find_gcf(numbers):
    if len(numbers) == 0:
        return None
    gcf = numbers[0]
    for num in numbers[1:]:
        gcf = gcd(gcf, num)
    return gcf 

t = i()
a = l()
b = l()
dic = defaultdict(int)

count = 0
for i in range(t):
    gc = find_gcf([abs(a[i]), abs(b[i])])
    if a[i] != 0:
        simple_b = b[i] // gc
        simple_a = a[i] // gc
        if simple_b >= 0 and simple_a < 0:
            num = (- simple_b , abs(simple_a))
        elif simple_b < 0 and simple_a < 0:
            num = (abs(simple_b) , abs(simple_a))
        else:
            num = (simple_b , simple_a)
        dic[num] += 1 
    elif b[i] == 0:
        count += 1
    
# print(dic)    
maxx = 0
for val in dic.values():
    maxx = max(maxx, val)
print(maxx + count)
        