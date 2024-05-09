class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(n):
            if n == 0:
                return nums[0]
            elif n == 1:
                return max(nums[0], nums[1])
            return max(dp(n-2) + nums[n], dp(n-1))
        return dp(len(nums) - 1)