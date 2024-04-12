from collections import defaultdict
size_array, size_ops, size_query = int(input().split())
array = list(map(int, input().split()))
ops = []
for i in range(1, size_ops+1):
    ops.append(list(map(int, input().split())))
qur = []
for i in range(1, size_query+1):
    qur.append(list(map(int, input().split())))

pre_ops = [0] * (size_ops + 1)
for i in range(1, size_query + 1):
    pre_ops[i] = pre_ops[i - 1] + ops[i - 1]

pre_qur = [0] * (size_query + 1)
for i in range(1, size_query + 1):
    pre_qur[i] = pre_qur[i - 1] + qur[i - 1]
