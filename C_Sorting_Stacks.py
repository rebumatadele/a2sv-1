t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    carry = 0
    for i, val in enumerate(lst):
        if val > i:
            carry += val - i
        elif val == i:
            continue
        else:
            carry -= i - val
        if carry < 0:
            print("NO")
            break
    else:
        print("YES")