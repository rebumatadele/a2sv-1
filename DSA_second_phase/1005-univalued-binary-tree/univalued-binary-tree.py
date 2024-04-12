# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        #We're working with a tree
        que = deque([root])
        value = root.val
        while que:
            current = que.popleft()
            if current.val != value:
                return False
            if current.left:
                que.append(current.left)
            if current.right:
                que.append(current.right)
        return True