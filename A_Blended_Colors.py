t = int(input())
for _ in range(t):
    col = int(input())
    string = input()
    string2 = input()
    if string.count("R") == string2.count("R"):
        for i in range(col):
            if string[i] == "R" and string2[i] != "R":
                print("NO")
                break
        else:
            print("YES")                    
    else:
        print("NO")
