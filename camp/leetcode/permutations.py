class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        bucket = []
        k = len(nums)
        def backtrack():
            if len(bucket) == k:
                res.append(bucket[::])
                return
            for j in nums:
                if j in bucket:
                    continue
                bucket.append(j)
                backtrack()
                bucket.pop()
        backtrack()
        return res