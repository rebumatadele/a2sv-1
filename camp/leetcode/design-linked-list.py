class Node:
    def __init__(self, value=0):
        self.val = value
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.dummy = Node()
    def get(self, index: int) -> int:
        current = self.dummy.next
        i = 0
        while current:
            if i == index:
                return current.val
            i += 1
            current = current.next
        return -1

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.dummy.next
        self.dummy.next = newNode

    def addAtTail(self, val: int) -> None:
        current = self.dummy
        while current.next:
            current = current.next
        newNode = Node(val)
        current.next = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        current = self.dummy
        i = -1
        while current:
            if i == index - 1:
                newNode = Node(val)
                newNode.next = current.next
                current.next = newNode
                return
            i += 1
            current = current.next


    def deleteAtIndex(self, index: int) -> None:
        current = self.dummy
        i = -1
        while current and current.next:
            if i == index - 1:
                current.next = current.next.next
            i += 1
            current = current.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)