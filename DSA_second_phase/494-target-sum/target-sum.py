class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dp(current, j):
            if j == len(nums) and current == 0:
                return 1

            if j >= len(nums):
                return 0
            if (current, j) not in memo:
                memo[(current, j)] += dp(current + nums[j], j+1) 
                memo[(current, j)] += dp(current - nums[j], j+1)

            return memo[(current, j)]    

        memo = defaultdict(int)

        ret = dp(target, 0)
        print(memo)
        return ret