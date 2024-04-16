# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        heapify(heap)
        for value in lists:
            while value:
                heappush(heap, value.val)
                value = value.next
        if heap:
            root = ListNode(heappop(heap))
            node = root
            while heap:
                root.next = ListNode(heappop(heap))
                root = root.next
            print(node)
            return node
        return None