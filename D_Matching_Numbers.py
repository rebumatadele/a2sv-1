for _ in range(int(input())):
    n = int(input())
    if n % 2 == 0:
        print("No")
    else:
        print("Yes")
        s = sum(range(1, 2 * n + 1))
        num = s // n
        sums = []
        add = n // 2 
        add = 0 - add
        for i in range(n):
            sums.append(num + add)
            add += 1  
        sums.sort(key = lambda x : x % 2 == 1)
        val = 1
        for num in sums:
            print(num - val, val)
            val += 1
