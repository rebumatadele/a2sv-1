class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        bucket = []
        k = len(nums)
        def backtrack(i):
            ans.append(bucket[::])
            for j in range(i, k):
                if nums[j] in bucket:
                    continue
                bucket.append(nums[j])
                backtrack(j+1)
                bucket.pop()
        backtrack(0)
        return ans