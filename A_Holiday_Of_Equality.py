n = int(input())
lst = []
lst = input().split()
lst = list(map(int, lst))
maximum = max(lst)
total = 0
for i in lst:
    total += maximum - i

print(total)