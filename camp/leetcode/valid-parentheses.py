class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == ")" or i =="}" or i == "]":
                if len(stack) <= 0:
                    return False
                val = stack[-1]
                #return False if i does not close val
                if val == "(":
                    if i ==")" :
                        stack.pop()
                    else:
                        return False 
                elif val == "{":
                    if i =="}" :
                        stack.pop()
                    else:
                        return False 
                elif val == "[":
                    if i =="]" :
                        stack.pop()
                    else:
                        return False 
                continue
            
            stack.append(i)
        if len(stack) > 0:
                return False
        return True
