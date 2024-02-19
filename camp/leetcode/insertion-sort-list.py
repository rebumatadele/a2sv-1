# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_sorted = ListNode(0)
        head_sorted.next = head
        tail = head
        current = head.next

        while current:
            if current.val >= tail.val:
                tail = current
                current = tail.next
            else:
                tail.next = current.next
                #find the position to insert the current
                pos = head_sorted
                while pos.next.val < current.val:
                    pos = pos.next
                current.next = pos.next
                pos.next = current

                current = tail.next
        return head_sorted.next