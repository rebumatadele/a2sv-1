class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        bucket = []
        k = len(nums)
        def backtrack(i):
            ans.append(bucket[:])
            for j in range(i, k):
                if j > i and nums[j] == nums[j-1]:
                    continue
                bucket.append(nums[j])
                backtrack(j+1)
                bucket.pop()
        nums.sort()
        backtrack(0)
        return ans
