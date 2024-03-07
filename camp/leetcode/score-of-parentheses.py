class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        for i in s:
            if i == "(":
                stack.append("(")
            else:
                if stack[-1] == "(":
                    stack.pop()
                    stack.append(1)
                else:
                    inner_score = 0
                    while stack[-1] != "(":
                        inner_score += stack.pop()
                    stack.pop()
                    stack.append(2 * inner_score)
        for i in stack:
            score += i
        return score