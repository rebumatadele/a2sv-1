n = int(input())
string = input()
for i in range(n-1):
    if string[i] > string[i+1]:
        print("YES")
        print(i+1, i+2)
        break
else:
    print("NO")