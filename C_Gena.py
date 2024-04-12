aastu = int(input())
array1 = list(map(int, input().split()))
addis = int(input())
array2 = list(map(int, input().split()))

array1.sort()
array2.sort()
count = 0
i = 0
j = 0
while i<aastu and j < addis:
    if array1[i] == array2[j] or abs(array1[i] - array2[j]) == 1:
        count +=1
        j +=1
        i +=1
    elif array1[i] < array2[j]:
        i +=1
    elif array1[i] > array2[j]:
        j +=1
print(count)