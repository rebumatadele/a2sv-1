
for _ in range(int(input())):
    size, d = list(map(int, input().split()))
    s = list(map(int, input()))
    ans = []
    flag = False
    for i in range(len(s)):
        if not flag and int(s[i]) < d:
            flag = True
            ans.append(str(d))
        ans.append(str(s[i]))
    if not flag:
        ans.append(str(d))
    print(int("".join(ans)))
    
    