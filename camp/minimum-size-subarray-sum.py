class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum_ = 0
        length = float('inf')
        left = 0
        for i in range(len(nums)):
            sum_ += nums[i]
            while sum_ >= target:
                length = min(length, i - left + 1)
                sum_ = sum_ - nums[left]
                left += 1
        if length == float('inf'):
            return 0
        return length