
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fastNode = head
        slowNode = head

        while fastNode.next:
            if fastNode.next.next != None:
                fastNode = fastNode.next.next
            else:
                fastNode = fastNode.next
            slowNode = slowNode.next
        return slowNode
