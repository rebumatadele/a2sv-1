t = int(input())
for _ in range(t):
    n = int(input())
    word = input()
    vowel = ["a","e"]
    cons = ["b", "c", "d"]
    lst = []
    word = word[::-1]
    i = 0 
    while i < len(word):
        if word[i] in cons:
            for j in range(i, i+3):
                lst.append(word[j])
            lst.append(".")
            i +=3
        elif word[i] in vowel:
            for j in range(i, i+2):
                lst.append(word[j])
            lst.append(".")
            i +=2
    lst.pop()
    lst = lst[::-1]
    res = "".join(lst)
    print(res)
    
    
    
        
                
            
            
        