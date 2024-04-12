import sys

def i():
    return int(sys.stdin.readline().strip())

def l(): 
    return list(map(int, sys.stdin.readline().strip().split()))

def s():
    return sys.stdin.readline().strip()

def d():
    return [int(digit) for digit in input()]

n, k = l()
acc = l()
left = min(acc)
right = (sum(acc) / n) + 1
# right = max(acc)
def helper(mid):
    gain = 0
    need = 0
    for val in acc:
        if val > mid:
            temp = val - mid
            gain += temp - (temp * k)/ 100
        elif val < mid:
            need += mid - val
    return gain >= need

while right - left > 10 ** -7:
    mid = (left + right) / 2
    if helper(mid):
        left = mid
    else:
        right = mid
else:
    print(right)