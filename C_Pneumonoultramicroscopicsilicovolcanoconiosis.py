def abr():
    t = int(input())
    for _ in range(t):
        string = input()
        if len(string)<=10:
            print(string)
        if len(string)> 10:
            num = len(string) - 2 
            abr = string[0] + str(num) + string[num+1]
            print(abr)
abr()