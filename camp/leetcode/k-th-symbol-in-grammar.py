class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        kMax = n -1
        kMax = 2 ** kMax
        rev = 0
        if k == 1:
            return 0
        if k <= int(kMax/2):
            ret = self.kthGrammar(n-1, k)
        else:
            rev += 1
            ret = self.kthGrammar(n-1, (k - int(kMax/2)))
        if rev:
            return abs(ret-rev)
        else:
            return ret
        

        