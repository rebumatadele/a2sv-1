t = int(input())  

for _ in range(t):
    temp = int(input()) 
    stre = tuple(map(int, input().split())) 
     
    prefix_max = [0] * len(stre) 
    prev_max = [0] * len(stre) 
    
    prefix_max[0] = stre[0] 
    prev_max[-1] = stre[-1] 
     
    for i in range(1, len(stre)):
        prefix_max[i] = max(prefix_max[i-1], stre[i]) 
    for i in range(len(stre)-2, -1, -1):
        prev_max[i] = max(prev_max[i+1], stre[i])
    for i in range(len(stre)):
        print(stre[i] - max(prefix_max[i-1] if i-1 >= 0 else 0, prev_max[i+1] if i+1 < len(stre) else 0), end=' ')
    print()