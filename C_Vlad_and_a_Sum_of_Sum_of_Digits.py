t = int(input())
for _ in range(t):
    num = int(input())
    # s = 0
    # for i in range(1, num + 1):
    #     lst = list(map(int, str(i)))
    #     s += sum(lst)
    # print(s)
    s = 0
    for i in range(1, num + 1):
        digit_sum = 0
        current_num = i

        while current_num > 0:
            digit_sum += current_num % 10
            current_num //= 10

        s += digit_sum

    print(s)
