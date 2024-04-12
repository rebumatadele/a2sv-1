import math
t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    sum_ = sum(lst)
    if sum_ == (int(math.sqrt(sum_)) * int(math.sqrt(sum_))):
        print("YES")
    else:
        print("NO")