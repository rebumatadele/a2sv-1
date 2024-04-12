t = int(input())
for _ in range(t):
    arr1 = input().split()
    # print(arr1)
    arr2 = arr1[1:]
    # print(arr2)
    kenenisa = arr1[0]
    count = 0
    for i in range(1, 4):
        if int(arr1[i])>int(kenenisa):
            count +=1
    print(count)