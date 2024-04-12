t = int(input())
for _ in range(t):
    lst = input().split()
    for i in range(3):
        if lst[0] == lst[1]:
            print(lst[2])
            break
        elif lst[0] == lst[2]:
            print(lst[1])
            break
        else:
            print(lst[0])
            break
            
    