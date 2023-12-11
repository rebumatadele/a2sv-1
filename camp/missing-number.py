class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums)

        for i in range(len(nums)):
            if i == nums[i]:
                continue
            else:
                return i
        if length not in nums:
                return length
        return 0
