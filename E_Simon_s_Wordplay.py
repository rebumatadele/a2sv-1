t = int(input())
for _ in range(t):
    n = int(input())
    string = ""
    lst = []
    for i in range(n):
        temp = input()
        lst.append(temp)
        string +=temp
    rest = len(set(lst)) - 1
    a = string.count("a")
    b = string.count("b")
    c = string.count("c")
    d = string.count("d")
    e = string.count("e")

    if a == max(a, b, c, d, e):
        let = "a"
    if b == max(a, b, c, d, e):
        let = "b"
    if c == max(a, b, c, d, e):
        let = "c"
    if d == max(a, b, c, d, e):
        let = "d"
    if e == max(a, b, c, d, e):
        let = "e"
    fac = 1
    if a == b or a ==c or a ==d or  a ==e:
        fac= 2
        
    # print(max(a, b, c, d, e)) 
    mi = 0
    ma = 0  
    for i in lst:
        if mi >= max(a, b, c, d, e):
            print(ma)
            break
        st = set(i)
        if let in st:
            mi += len(i) - i.count(let)
        else:
            mi += len(i)
        ma +=1
    else:
        if mi < max(a, b, c, d, e):
            print(ma)
        else:
            print(0)
        
            