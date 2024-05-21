class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def backtrack(bucket, j):
            if j == n:
                palindrome.append(bucket[:])
                return

            for i in range(j+1, n+1):
                val = s[j:i]
                if val == val[::-1]:
                    bucket.append(val)
                    backtrack(bucket, i)
                    bucket.pop()
        
        n = len(s)
        palindrome = []
        backtrack([], 0)
        # print(palindrome)
        return palindrome
        


