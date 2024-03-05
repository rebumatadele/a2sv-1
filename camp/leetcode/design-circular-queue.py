class MyCircularQueue:

    def __init__(self, k: int):
        self.que = []
        self.k = k

    def enQueue(self, value: int) -> bool:
        if len(self.que) < self.k:
            self.que.append(value)
            return True
        return False

    def deQueue(self) -> bool:
        if len(self.que) == 0:
            return False
        self.que.pop(0)
        return True

    def Front(self) -> int:
        if len(self.que) > 0:
            return self.que[0]
        return -1

    def Rear(self) -> int:
        if len(self.que) > 0:
            return self.que[-1]
        return -1

    def isEmpty(self) -> bool:
        if len(self.que) == 0:
            return True
        else:
            return False
    def isFull(self) -> bool:
        if len(self.que) == self.k:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()