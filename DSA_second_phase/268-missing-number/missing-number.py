class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.append(-1)
        i = 0
        while i < len(nums):
            if nums[i] == -1 or nums[i] == i:
                i += 1
                continue
            curr = nums[i]
            nums[i], nums[curr] = nums[curr], nums[i]
        for i in range(len(nums)):
            if nums[i] == -1:
                return i

            