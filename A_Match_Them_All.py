from collections import Counter, defaultdict
t = int(input())
for _ in range(t):
    dic = defaultdict(int)
    n = int(input())        
    inp = []
    for i in range(n):
        inp.append(input())  
    for i in inp:
        for j in i:
            dic[j] += 1
    for key, val in dic.items():
        if val < n or val % n != 0:
            print("NO")
            break
    else:
        print("YES")
    
        
    