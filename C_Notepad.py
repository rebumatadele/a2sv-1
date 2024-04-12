from collections import defaultdict
size=int(input())
for _ in range(size):
    length=int(input())
    arr=input()
    my_arr=set()
    for i in range(1,len(arr)-1):
        if arr[i:i+2] in my_arr:
            print("YES")
            break
        else:
            my_arr.add(arr[i-1:i+1])
    else:
        print("NO")