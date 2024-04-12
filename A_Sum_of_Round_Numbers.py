import sys

def i():
    return int(sys.stdin.readline().strip())

def l(): 
    return list(map(int, sys.stdin.readline().strip().split()))

def ls():
    return sorted(list(map(int, sys.stdin.readline().strip().split())))
def s():
    return sys.stdin.readline().strip()

def d():
    return [int(digit) for digit in input()]

for _ in range(i()):
    num = d()
    res = []
    n = len(num)
    for i, val in enumerate(num):
        if val == 0:
            continue
        if i + 1 == n:
            res.append(str(val))
        else:
            res.append(str(val * (10 ** (n - (i + 1)))))
    print(len(res))
    print(" ".join(res))