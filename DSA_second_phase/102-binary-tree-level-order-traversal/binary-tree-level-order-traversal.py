# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root: return []
        que = deque([root])
        res = []

        while que:
            l = len(que)
            temp = []
            
            for _ in range(l):
                node = que.popleft()
                temp.append(node.val)

                if node.left:
                    que.append(node.left)

                if node.right:
                    que.append(node.right)

            res.append(temp)

        return res
