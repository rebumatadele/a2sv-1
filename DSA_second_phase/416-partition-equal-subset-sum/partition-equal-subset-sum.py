class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        def dp(target, j):
            if target == 0:
                return True
            if j >= len(nums):
                return False
            if target < 0:
                return False
            if (target, j) not in memo:
                memo[(target, j)] = (dp(target-nums[j], j+1) or dp(target, j+1))
            return memo[(target, j)]
    
        if sum(nums) % 2 == 1:
            return False
        
        memo = defaultdict(int)
        target = sum(nums)/2
        # nums.sort()
        return dp(target, 0)


