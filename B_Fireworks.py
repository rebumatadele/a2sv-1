import sys

def i():
    return int(sys.stdin.readline().strip())

def l(): 
    return list(map(int, sys.stdin.readline().strip().split()))

def s():
    return sys.stdin.readline().strip()
for _ in range(i()):
    a, b, m = l()
    count = 0
    count += (a + m)//a + (b + m)//b
    print(count)