n = int(input())
string =""
lst = []
for i in range(n):
    temp = input()
    lst.append(temp)
    string +=temp
    
lst.sort(key = len, reverse=True)

for i in range(1, len(lst)):
    if lst[i] not in lst[i-1]:
        print("NO")
        break
else:
    print("YES")
    for i in lst[::-1]:
        print(i)