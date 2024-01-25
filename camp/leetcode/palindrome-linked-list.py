# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        #Find the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow
        prev = None
        #Flip the elements starting from the middle
        while middle:
            nex = middle.next
            middle.next = prev
            prev = middle
            middle = nex
        #now prev is the middle element
        # print(prev)

        #check if they're equal            
        while prev:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
        return True
