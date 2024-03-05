class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
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
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                bucket.append(candidates[j])
                backtrack(j+1)
                bucket.pop()
        candidates.sort()
        backtrack(0)
        return ans
