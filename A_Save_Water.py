num_cont = int(input())
vol = int(input())
lst = []
for _ in range(num_cont):
    lst.append(int(input()))
lst.sort(reverse = True)
total = 0
k = 0
for i in lst:
    total += i
    k +=1
    if total >= vol:
        print(k)
        break        
    