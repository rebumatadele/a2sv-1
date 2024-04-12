n = int(input())
lst = list(map(int, input().split()))
q = int(input())

total = [0] * (n + 1)
sorted_total = [0] * (n + 1)

for i in range(1, n + 1):
    total[i] = total[i - 1] + lst[i - 1]

sor = sorted(lst)
for i in range(1, n + 1):
    sorted_total[i] = sorted_total[i - 1] + sor[i - 1]

for _ in range(q):
    type, left, right = map(int, input().split())
    if type == 1:
        print(total[right] - total[left - 1])
    else:
        print(sorted_total[right] - sorted_total[left - 1])