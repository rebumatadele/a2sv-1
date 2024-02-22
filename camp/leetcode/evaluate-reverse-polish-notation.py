class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+" or i == "-" or i == "*" or i == "/":
                ans = 0
                var1 = stack[-1]
                stack.pop()
                var2 = stack[-1]
                stack.pop()
                if i == "+":
                    ans = var1 + var2
                    stack.append(ans)
                if i == "-":
                    ans = var2 - var1
                    stack.append(ans)
                if i == "*":
                    ans = var1 * var2
                    stack.append(ans)
                if i == "/":
                    ans = int(var2 / var1)
                    stack.append(ans)
            else:
                stack.append(int(i))
            # print(stack)
        return stack[-1]
            
