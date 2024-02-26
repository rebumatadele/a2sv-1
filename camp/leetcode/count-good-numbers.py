class Solution:
    def countGoodNumbers(self, n: int) -> int:
        odd = n // 2
        even = ceil(n/2)                  
        return (self.power(5, even) * self.power(4, odd)) % (10**9 + 7)
    def power(self, x, y):
        if y == 0:
            return 1  
        res = self.power(x, int(y/2))
        res *= res   
        res %= (10**9 + 7) 
        if y % 2:
            res *= x
        res %= (10**9 + 7)
        return res