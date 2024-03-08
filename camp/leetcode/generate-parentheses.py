class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        bucket = []
        def helper(o, c):
            if o == c == n:
                ans.append("".join(bucket))
                return
            if o < n:
                bucket.append("(")
                helper(o + 1, c)
                bucket.pop()
            if o > c:
                bucket.append(")")
                helper(o, c + 1)
                bucket.pop()
        helper(0, 0)
        return ans
