def codeforce():
    t = int(input())
    codeforce = ["c", 'o', 'd','e','f','o','r','c','e','s']
    for _ in range(t):
        c = input()
        if c in codeforce:
            print("YES")
        else:
            print("NO")
codeforce()