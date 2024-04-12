n, m = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
print(arr1)
print(arr2)

lst = []
i = 0
j = 0
while j <m and i <n:
        if arr1[i] <= arr2[j]:
            lst.append(arr1[i])
            i +=1
        elif i == len(arr1)-1 or j == len(arr2)-1:
            lst.extend(arr1[i:])   
            lst.extend(arr2[j:]) 
            break  
        else:
            lst.append(arr2[j])
            j +=1 


print(lst)
res = " ".join(map(str, lst))
print(res)