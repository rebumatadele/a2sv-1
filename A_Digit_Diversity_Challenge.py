left, right = map(int, input().split())

for i in range(left, right+1):
    digits = set()
    
    for digit in str(i):
        if digit in digits:
            break
        digits.add(digit)
        
    else:
        print(i)
        break

else:
    print(-1)
