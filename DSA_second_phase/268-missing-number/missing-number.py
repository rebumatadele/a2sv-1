class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # s = sum(nums)
        # n = (len(nums) * (len(nums) + 1)) /2
        # return int(n - s)
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return max(nums) + 1
            
