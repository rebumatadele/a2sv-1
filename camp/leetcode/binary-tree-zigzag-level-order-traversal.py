# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def zig(node, level, dic):
            if not node:
                return dic
            dic = zig(node.left, level+1, dic)
            if level not in dic:
                dic[level] = []
            dic[level].append(node.val)
            dic = zig(node.right, level+1, dic)
            return dic
        dic = sorted(zig(root, 0, {}).items())
        lst = []
        for i, (key, val) in enumerate(dic):
            if i % 2:
                val = val[::-1]
                lst.append(val)
                continue
            lst.append(val)
        return lst
            
            


        