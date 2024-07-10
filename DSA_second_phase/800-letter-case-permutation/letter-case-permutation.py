class Solution(object):
    def letterCasePermutation(self, S):
        def backtrack(bucket="", i=0):
            if len(bucket) == len(S):
                res.append(bucket)
            else:
                if S[i].isalpha():
                    backtrack(bucket + S[i].swapcase(), i + 1)
                backtrack(bucket + S[i], i + 1)
                
        res = []
        backtrack()
        return res