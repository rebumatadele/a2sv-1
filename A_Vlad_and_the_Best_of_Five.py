t = int(input())
for _ in range(t):
    string = input()
    lst = list(string)
    a = lst.count("A")
    if a > len(lst)/2:
        print("A")
    else:
        print("B")