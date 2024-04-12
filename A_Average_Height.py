t = int(input())

for _ in range(t):
    n = int(input())
    height = input().split()
    height = list(map(int, height))
    n = n-1
    i = 0
    while i<n:
            if height[i] % 2 ==1 and height[n] % 2 ==0:
                #swap
                temp = height[i]
                height[i] = height[n]
                height[n] = temp
                n-=1
            elif height[i] % 2 ==1 and height[n] % 2 ==1:
                n -=1
            elif  height[i] % 2 ==0 and height[n] % 2 ==0:
                i+=1
            elif height[i] % 2 ==0 and height[n] % 2 ==1:
                i+=1
                n-=1
    print(*height, (" "))
        
            