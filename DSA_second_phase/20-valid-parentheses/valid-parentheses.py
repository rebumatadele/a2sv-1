class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        charmap = {
            "]" : "[",
            "}" : "{",
            ")" : "("
        }
        for el in s:
            if el != ")" and el != "}" and el != "]":
                stack.append(el)
                continue
            if not stack or stack[-1] != charmap[el]:
                return False
            stack.pop() 
        return len(stack) == 0