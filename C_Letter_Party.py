n, k = map(int, input().split())
from collections import defaultdict
s = input()
dic = defaultdict(int)
left = 0
maximum = 0
for r in range(n):
    dic[s[r]] += 1
    if dic['a'] > k and dic['b'] > k:
        dic[s[left]] -= 1
        left += 1
    maximum = max(maximum, r-left +1)
print(maximum)