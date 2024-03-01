# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # if not root.left or not root.right:
        #     return False
        def symmetry(node1, node2):
            if not node1 and not node2:
                return True
            elif (node1 and (not node2))or ((not node1) and node2):
                return False
            res = node1.val == node2.val and  symmetry(node1.left, node2.right) and symmetry(node1.right, node2.left)
            return res
        return(symmetry(root.left, root.right))
            