import sys

def i():
    return int(sys.stdin.readline().strip())

def l():
    return list(map(int, sys.stdin.readline().strip().split()))

def s():
    return sys.stdin.readline().strip()

from bisect import bisect_right
s, b = l()
attack = l()

emp = []
for _ in range(b):
    defense, gold = l()
    emp.append([defense, gold])    
emp.sort()

emp_gold = []
emp_defense = []
total = 0
emp_gold.append(0)
for i in emp:
    emp_defense.append(i[0]) 
    total += i[1]
    emp_gold.append(total)

res = []
for i in attack:
    res.append(str(emp_gold[bisect_right(emp_defense, i)]))
print(" ".join(res))
