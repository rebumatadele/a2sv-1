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
    n, k = l()
    ne = True
    ke = True
    if n % 2 == 1:
        ne = False
    if k % 2 == 1:
        ke = False
    if not ne and ke:
        print("NO")
        continue
    res = []
    if ne and ke:
        for i in range(k):
            res.append(str(n//k))
        print("YES")
        print(" ".join(res))
    elif not ne and not ke:
        x = (n // k)
        if x % 2 != 1:
            x = (n // k) + 1 
        dif = n - (x * (k - 1))
        if dif < 0:
            print("NO")
            continue
        for _ in range(k - 1):
            res.append(str(x))
        res.append(str(dif))
        print("YES")
        print(" ".join(res))
    else:
        x = (n // k)
        if x % 2 == 1:
            x = (n // k) + 1
        dif = n - (x * (k - 1))
        if dif < 0:
            print("NO")
            continue
        for _ in range(k - 1):
            res.append(str(x))
        res.append(str(dif))
        print("YES")
        print(" ".join(res))
        
        
    