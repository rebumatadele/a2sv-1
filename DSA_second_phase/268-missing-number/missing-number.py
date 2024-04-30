class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = sum(nums)
        n = (len(nums) * (len(nums) + 1)) /2
        return int(n - s)
