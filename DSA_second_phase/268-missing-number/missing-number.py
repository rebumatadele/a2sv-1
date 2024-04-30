class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # s = sum(nums)
        # n = (len(nums) * (len(nums) + 1)) /2
        # return int(n - s)
        # nums.sort()
        # for i in range(len(nums)):
        #     if i != nums[i]:
        #         return i
        # return max(nums) + 1
            
        arr = 0
        ran = 0
        for i, val in enumerate(nums):
            arr ^= val
            ran ^= i + 1
        return arr ^ ran