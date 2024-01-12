class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ones = 0
        res = 0
        i = 0
        for j in range(len(nums)):
            ones += nums[j]
            if j - i + 1 - ones > k:
                ones -= nums[i]
                i += 1
            res = max(res, j - i + 1)
        return res