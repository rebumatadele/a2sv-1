# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        new_head = ListNode(next=head)
        
        
        leftmost = new_head
        for _ in range(left -1) :
            leftmost = leftmost.next
        prev = None 
        rev = leftmost.next
        print(rev)
        for _ in range(left,  right + 1):
            rev.next, prev, rev = prev, rev, rev.next
            
        leftmost.next.next = rev
        leftmost.next = prev
        return new_head.next