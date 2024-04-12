t = int(input())
for _ in range(t):
    string = input()
    if len(string)==2:
        print(string)       
    else:
        new_str = ""
        for i in range(0, len(string), 2):
            new_str +=string[i:i+1]
        new_str +=string[-1]
        print(new_str)