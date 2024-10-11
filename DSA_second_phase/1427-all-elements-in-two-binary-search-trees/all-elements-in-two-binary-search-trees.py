# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        arr = []
        def getElements(root):
            if root is None:
                return None
            arr.append(root.val)
            return getElements(root.left) or getElements(root.right)
        
        getElements(root1)
        getElements(root2)

        return sorted(arr)