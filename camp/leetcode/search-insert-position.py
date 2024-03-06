class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = -1
        right = len(nums)
        while left + 1 < right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid
            else:
                left = mid
        return right