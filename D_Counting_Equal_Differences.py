t =int(input())

for _ in range(t):
    n=int(input())
    temp = input().split()
    a=list(map(int, temp))
    counter ={}
    for i in range(n):
        if (a[i]-i) in counter:
            counter[(a[i]-i)] +=1
        else:
             counter[(a[i]-i)] =1
    res =0
    for key,value in counter.items():
        if value >1:
            for i in range(value):
                res+=i
    print(res)