t = int(input())
for _ in range(t):
    array = []
    for i in range(3):
        a = list(map(str, input()))
        array.append(a)
    print(array)
    for r in range(3):
        for c in range(3):
            if array[r][c] == "?":
                string = "ABC"
                for i in string:
                    if i not in array[r]:
                        print(i)
                    
                
                
         