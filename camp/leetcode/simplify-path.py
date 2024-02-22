class Solution:
    def simplifyPath(self, path: str) -> str:
        lst = path.split("/")
        stack = []
        i = 0
        print(lst)
        for i in lst:
            if i == "" or i == ".":
                continue
            elif i == "..":
                if stack:
                    stack.pop()
                continue
            stack.append(i)
        ans = "/" + "/".join(stack)
        
        return ans