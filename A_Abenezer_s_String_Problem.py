t = int(input())
for _ in range(t):
    n = int(input())
    string = input()
    max_ = max(string)
    print(ord(max_.lower()) - ord('a') + 1)