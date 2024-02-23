class MyStack:

    def __init__(self):
        self.q1 = deque()
        # q2 = deque()

    def push(self, x: int) -> None:
        self.q1.appendleft(x)

    def pop(self) -> int:
        res = self.q1.popleft()
        return(res)

    def top(self) -> int:
        res = self.q1[0]
        return res
    def empty(self) -> bool:
        if self.q1:
            return False
        else:
            return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()