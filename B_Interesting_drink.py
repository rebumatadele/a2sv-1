from bisect import bisect_right
shops = int(input())
x = list(map(int, input().split()))
x.sort()
for i in range(int(input())):
    print(bisect_right(x, int(input())))