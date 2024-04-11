# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def dfs(node):
            if node is None:
                return None
            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if node.val in delete:
                if node.left:
                    res.append(node.left)
                if node.right:
                    res.append(node.right)
                return None
            return node
        res = []
        delete = set(to_delete)
        node = dfs(root)
        if node:
            res.append(node)
        return res

