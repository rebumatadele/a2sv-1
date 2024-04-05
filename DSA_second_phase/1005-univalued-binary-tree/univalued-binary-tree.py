# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        visited = set([root])
        queue = deque([root])
        f = root.val
        
        while queue:
            node = queue.popleft()
            if node.val != f:
                return False
            if node.left:
                queue.append(node.left)  
            if node.right:
                queue.append(node.right)  
        return True