t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    string = input().strip()

    cnt = string[:k].count("W")
    # print(string, cnt, k)

    ans = cnt
    # cnt = 0
    for i in range(k, len(string)):  
        if string[i] == "W":
            cnt += 1
            # print("hello", temp, string[i], i)
        if string[i - k] == "W":
            cnt -= 1
        ans = min(ans, cnt)
        # print(i, i - k, cnt)
        # if cnt == 0:
        #     # print(0)
        #     break

    
    print(ans)
# BBWBW
#     |
#     |     
# cnt = 1   