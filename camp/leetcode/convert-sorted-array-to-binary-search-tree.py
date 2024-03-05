# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dc(left, right):
            if left > right:
                return None
            m = (left + right) // 2
            root = TreeNode(nums[m])
            root.left = dc(left, m - 1)
            root.right = dc(m + 1, right)
            return root
        root = dc(0, len(nums)-1)
        return root