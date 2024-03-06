class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = -1
        right = len(nums)
        while left + 1 < right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid
            else:
                right = mid
        if right >= len(nums) or nums[right] != target:
            return [-1, -1]
        l = right -1
        r = len(nums)
        while l + 1 < r:
            mid = (l + r) // 2
            if target < nums[mid]:
                r = mid
            else:
                l = mid
        return [right, l]

