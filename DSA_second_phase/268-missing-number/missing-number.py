class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        small = 0
        large = 0
        i = 0
        while i < n-1:
            small ^= i
            large ^= nums[i]
            i += 1
        small ^= i
        return small ^ large




