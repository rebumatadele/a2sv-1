for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    min_operation = 0
    max_ = max(a)  
    for val in a:
        min_operation = max(min_operation, max_ - val)

    print(min_operation)
