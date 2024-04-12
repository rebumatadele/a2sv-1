t =int(input())
for _ in range(t):
    size = int(input())
    string= input()
    array = []
    look = 1
    current = 0
    while look < size:
        if string[current] == string[look]:
            array.append(string[current])
            current = look +1
            look = current+1
            
        else:
            look+=1
    res = "".join(array)
    print(res)