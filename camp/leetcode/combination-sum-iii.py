class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        bucket = []
        def backtrack(i):
            if len(bucket) == k:
                if sum(bucket) == n:
                    res.append(bucket[:])
                return 
            for j in range(i, 10):
                if j in bucket:
                    continue
                bucket.append(j)
                backtrack(j+1)
                bucket.pop()
        backtrack(1)
        return res
