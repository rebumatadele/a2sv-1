# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while (slow and slow.next):
            fast = fast.next
            slow = slow.next.next
            if (fast == slow):
                fast = head
                while (fast != slow):
                    fast = fast.next
                    slow = slow.next
                return slow
        return None