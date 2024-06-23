class Solution(object):
    def pivotIndex(self, nums):
        left_sum = 0
        right_sum = 0
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1