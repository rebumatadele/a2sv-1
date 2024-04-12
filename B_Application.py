from collections import defaultdict
t = int(input())
db = []
dic = defaultdict(int)
for _ in range(t):
    name = input()
    if dic[name]==False:
        dic[name]= 1
        print("OK")
    else:
        print(name+str(dic[name]))
        dic[name] +=1 
    