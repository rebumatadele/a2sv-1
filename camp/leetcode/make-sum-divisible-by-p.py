class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = sum(nums) % p
        if n == 0:
            return 0
        ans = len(nums)
        rem = 0
        rightmost_rem = {0: -1}
        for i in range(len(nums)):
            rem = (rem + nums[i]) % p
            r = (rem - n) % p

            if r in rightmost_rem:
                j = rightmost_rem[r]
                ans = min(ans, i - j)
            rightmost_rem[rem] = i
        if ans < len(nums):
            return ans
        return -1
        