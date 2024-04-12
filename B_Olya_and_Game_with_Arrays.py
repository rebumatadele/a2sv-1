t = int(input())
for _ in range(t):
    num = int(input())
    
    lst = []
    for i in range(num):
        #description of array
        num_el = int(input())
        arr = list(map(int, input().split()))
        arr.sort()
        lst.append(arr)
    lst.sort()
    total = lst[0][0]
    lst.sort(key= lambda x: x[1])
    for k in range(1, len(lst)):
        total += lst[k][1]
    print(total)