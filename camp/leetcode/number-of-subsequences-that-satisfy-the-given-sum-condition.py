class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        res = 0
        nums.sort()
        mod = 1000000007
        for i in range(len(nums)):
            current = target - nums[i]
            pos = bisect_right(nums, current)
            if pos != 0:
                pos -= 1
            else:
                continue
            if pos >= i:
                res +=  pow(2, pos-i, mod)
        return res % mod