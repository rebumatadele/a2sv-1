import math
t = int(input())
for _ in range(t):
    size = int(input())
    array = sorted(map(int, input().split()))
    left = 0
    right = size -1
    ac = 0
    count = 0
    while left <= right:
        count += array[left]
        ac += array[left]
        if ac >= array[right] and right != left:
            count += 1
            right -= 1
            left += 1
            ac = ac - array[right] 
        elif left == right -1:
            count -= array[left]
            count += math.ceil((ac + array[right]) / 2) + 1
            break
        else:
            left +=1
            
    print(count)