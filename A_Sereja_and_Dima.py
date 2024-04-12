n = int(input())
lst = list(map(int, input().split()))
i = 0
j = n -1
s = 0
d = 0
turn = 0
while i <= j:
    if turn == 0:
        s += max(lst[i], lst[j])
        if lst[i] > lst[j]:
            i +=1
        else:
            j -=1
        turn = 1
    else:
        d += max(lst[i], lst[j])
        if lst[i] > lst[j]:
            i +=1
        else:
            j -=1
        turn = 0
print(s, d)
        