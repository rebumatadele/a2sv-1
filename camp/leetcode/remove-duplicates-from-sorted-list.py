# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        current = head
        while current and current.next:
            nxt= current.next
            while nxt and current.val == nxt.val:
                nxt = nxt.next
            current.next = nxt
            current = nxt
        return head