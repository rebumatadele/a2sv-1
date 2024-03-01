# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:  
        def ran(node, low, high):
            if not node:
                return 0
            sum_ = 0
            if low <= node.val <= high:
                sum_ = node.val
            sum_ += ran(node.left, low, high)
            sum_ += ran(node.right, low, high)
            return sum_
        return ran(root, low, high)

