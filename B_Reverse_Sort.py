t = int(input())
for _ in range(t):
    n = int(input())
    binary = list(input())
    sorted_binary = sorted(binary)
    lst = []
    for i in range(len(sorted_binary)):
        if sorted_binary[i] != binary[i]:
            lst.append(i+1)
    length = len(lst)
    res = " ".join(map(str, lst))
    if length:
        print(1)
    print(length, res)