class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        curr = 0
        min_len = float("inf")
        for j in range(len(nums)):
            curr += nums[j]
            while curr >= target:
                min_len = min(min_len, j-i+1)
                curr -= nums[i]
                i += 1
        if sum(nums) < target:
            return 0
        else:
            return min_len