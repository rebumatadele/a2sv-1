# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before = ListNode(0)
        after = ListNode(0)
         
        current_befr = before
        current_aft = after
        while head:
            if head.val < x:
                current_befr.next, current_befr = head, head
            else:
                current_aft.next, current_aft = head, head
            
            head = head.next
        current_aft.next = None
        current_befr.next = after.next

        return before.next