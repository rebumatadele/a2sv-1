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
            temp = []
            for _ in range(l):
                current = que.popleft()
                temp.append(current.val)
                if current.left:
                    que.append(current.left)
                if current.right:
                    que.append(current.right)
            res.append(temp)    
        print(res)
        return res        