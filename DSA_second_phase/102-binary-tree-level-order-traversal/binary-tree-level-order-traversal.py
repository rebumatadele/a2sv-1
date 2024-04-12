# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        que = deque([root])
        res = []
        while que:
            l = len(que)
            res.append([current.val for current in que])

            for _ in range(l):
                current = que.popleft()
                if current.left:
                    que.append(current.left)
                if current.right:
                    que.append(current.right)
                    
        return res        