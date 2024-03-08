class MinStack:

    def __init__(self):
        self.stack = []
        self.small = float("inf")
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.stack:
            self.small = min(self.small, val)
    def pop(self) -> None:
       poped = self.stack.pop() 
       if poped == self.small:
            if self.stack:
               self.small = min(self.stack)
            else:
                self.small = float('inf')

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        if self.stack:
            return self.small
        return None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()