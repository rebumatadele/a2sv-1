n = int(input())
a = list(map(int, input().split()))
count = 0
start = 0
end = 0
i = 1
if len(a) == 1:
    print(0)
while i < len(a):
    if a[i] == a[i - 1] + 1:
        start = i-1
        while i < len(a) and a[i] == a[i-1] + 1:
            end = i
            i += 1
        count = max(count, end - start + 1)
    i += 1
one = 0
th = 0
if 1 in a:
    i = 1
    while i < len(a) and a[i] == a[i-1] + 1:
        end = i
        i += 1
    one = end + 1
if 1000 in a:
    i = len(a) -1
    end = len(a) -1
    while i > 0 and a[i] == a[i-1] + 1:
        i -= 1
        end = i  
    th = ((len(a) -1) - end) + 1
if one == count:
    count += 1
if th == count:
    count += 1
count -= 2
print(count)