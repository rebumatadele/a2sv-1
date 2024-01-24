# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        while fast and fast.next:
            if fast.next.next != None:
                fast = fast.next.next
            else:
                break
            head = head.next
            if head == fast:
                return True