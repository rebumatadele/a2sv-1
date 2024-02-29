# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, min_range = float('-inf'), max_range = float('+inf')):
            if not node: 
                return True
            if not(min_range < node.val < max_range):
                return False
            return(valid(node.left, min_range, node.val) and valid(node.right, node.val, max_range))
        return valid(root)
            

            
            

