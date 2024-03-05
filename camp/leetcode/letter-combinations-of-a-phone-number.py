class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }
        res = []
        bucket = []
        def backtrack(i):
            if len(bucket) == len(digits):
                if bucket:
                    res.append("".join(bucket[:]))
                return
            for j in range(len(dic[int(digits[i])])):
                bucket.append(dic[int(digits[i])][j])
                backtrack(i + 1)
                bucket.pop() 
        backtrack(0)
        return res

