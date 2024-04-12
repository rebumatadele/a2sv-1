code = "codeforces"
t = int(input())
for _ in range(t):
    string = input()
    counter =0
    for i in range(len(string)):
        if string[i] != code[i]:
            counter+=1
    print(counter)
    