# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
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
        ans = [0 for _ in range(len(res))]
        for i, val in enumerate(res):
            ans[i] = sum(val) / len(val)
        return ans