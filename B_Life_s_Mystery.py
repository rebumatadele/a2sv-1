string = input()
stack = []

for i in string:
    if stack and stack[-1] == i:
        while stack and stack[-1] == i:
            stack.pop()
    else:    
        stack.append(i)
res = "".join(stack)
print(res)