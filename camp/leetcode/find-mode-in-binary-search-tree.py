# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counter = Counter()

        def find(node, counter):
            if not node:
                return counter
            
            counter = find(node.left, counter)
            counter = find(node.right, counter)
            counter[node.val] += 1
            return counter
        find(root, counter)
        max_ = 0
        for key, val in counter.items():
            max_ = max(max_, val)
        res = []
        for key, val in counter.items():
            if val == max_:
                res.append(key)
        return res



