# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if not node:
                return []
            center = [node.val]
            left = inorder(node.left)
            right = inorder(node.right)
            return  left + center + right
        lst = inorder(root)
        def balance(lst):
            if not lst:
                return None
            node = TreeNode(lst[len(lst) //2])
            node.left = balance(lst[:len(lst) //2]) 
            node.right = balance(lst[len(lst) //2 + 1:]) 
            return node
        return balance(lst)

