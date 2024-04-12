n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
count = 0
j = 0
string = ""
for i in range(m):
    while j < n and arr2[i]>arr1[j]:
        count +=1
        j +=1
    string +=" "+ str(count)
    i+1
print(string)