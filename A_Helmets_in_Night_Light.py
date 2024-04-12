t = int(input())
for _ in range(t):
    n, first_cost = map(int, input().split())

    array1 = list(map(int, input().split()))
    array2 = list(map(int, input().split()))
    array = zip(array2, array1)
    
    array = sorted(array)
    array2, array1 = zip(*array)
    cost = 0
    cost = first_cost
    p = 1
    i = 0
    
    while p < n:
        if first_cost < array2[i]:
            cost += first_cost * (n-p)
            break
        
        if n-p < array1[i]:
            cost +=array2[i] * (n-p)
            break
            
        cost += array2[i] * array1[i]
        p +=array1[i]
        i = i+1
    print(cost)
            
                