class Solution:
    def sortSentence(self, s: str) -> str:
        lst = list(s.split())
        ans = [""] * len(lst)
        for val in lst:
            ans[int(val[-1]) -1] = val[:len(val)-1]
        return " ".join(ans)