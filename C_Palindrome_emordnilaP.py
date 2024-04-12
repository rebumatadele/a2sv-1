t =int(input())

for i in range(t):
    n=int(input())
    a=list(map(int,input().split())) 
    status = False
    indexes ={}
    ind = []
    for i in range(len(a)):
        if a[i]  in indexes:
            indexes[a[i]].append(i)
        else:
            indexes[a[i]] =[]
            indexes[a[i]].append(i)
    
    for key, value in indexes.items():
        value.sort()
        if value[0] < value[-1]-1:
            status=True
            break

    if status:
        print("YES")
    else:
        print("NO")