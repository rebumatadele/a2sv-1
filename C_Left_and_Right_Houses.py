import sys
import math
def i():
    return int(sys.stdin.readline().strip())
def l(): 
    return list(map(int, sys.stdin.readline().strip().split()))
def d():
    return [int(digit) for digit in input()]
def s():
    return sys.stdin.readline().strip()
for _ in range(i()):
    n = i()
    digits = d()
    one = digits.count(1)
    zero = len(digits) - one
    
    left = 0
    res = []
    if one >= len(digits)/2:
        res.append(0)
    for i in range(len(digits)):
        if digits[i] == 0:
            left += 1
        right = len(digits) - (i + 1)
        zero_on_right = zero - left
        one_on_right = right - zero_on_right
        if (left >= (i + 1) / 2 and one_on_right >= right / 2):
            res.append(i + 1)
    if res:
        if len(res) == 1:
            print(res[0])
        else:
            half = n / 2
            res.sort(key = lambda x :abs( half - x))
            print(res[0])
            