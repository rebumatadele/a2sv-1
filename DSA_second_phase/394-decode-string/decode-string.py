class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        size = len(s)
        indx = 0
        while indx < size:
            # populate the stack until a closing bracket comes up
            if s[indx] != "]":
                curr = []
                # if the character is a digit make it into a single digit
                while s[indx].isdigit():
                    curr.append(s[indx])
                    indx += 1
                # if it was a digit, add it into the stack
                if curr:
                    stack.append(int("".join(curr)))
                # Since we have increamented the indx we have to check again
                if s[indx] != "]":
                    stack.append(s[indx])
                    indx += 1  
                    continue
            current = []
            # once the closing bracket comes up store the values inside
            while stack[-1] != "[":
                current.append(stack.pop())
            current = "".join(current[::-1])

            #pop the bracket
            stack.pop()

            #get the digit
            num = int(stack.pop())

            #append the current string to the stack digit times
            for _ in range(num):
                stack.append(current)
            indx += 1
        return "".join(stack)