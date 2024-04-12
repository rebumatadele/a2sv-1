# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        #We're working with a tree
        stack = [root]
        value = root.val
        while stack:
            current = stack.pop()
            if current.val != value:
                return False
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        return True