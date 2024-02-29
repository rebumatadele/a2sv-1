class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pre={0:1}
        sum_ = 0
        ans = 0
        for i in nums:
            sum_ += i
            ans += pre.get(sum_-goal,0)
            pre[sum_] = pre.get(sum_,0) + 1
        return ans