class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        bucket = []
        k = len(candidates)
        def backtrack(i):
            if sum(bucket) == target:
                ans.append(bucket[:])
                return
            elif sum(bucket) > target:
                return
            for j in range(i, k):
                bucket.append(candidates[j])
                backtrack(j)
                bucket.pop()

        backtrack(0)
        return ans
