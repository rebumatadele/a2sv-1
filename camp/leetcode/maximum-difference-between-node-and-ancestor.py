# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def ans(node, ma, mi, md):
            if not node:
                return md
            ma = max(ma, node.val)
            mi = min(mi, node.val ) 
            md = max(md, ma - mi)
            md = ans(node.left, ma, mi, md)
            md = ans(node.right, ma, mi, md)
            return md
        return(ans(root, root.val, root.val, 0))