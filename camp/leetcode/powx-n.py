class Solution:
    def myPow(self, x: float, n: int) -> float:
        # bo = False
        # if n == 0:
        #     return 1
        # if n < 0:
        #     n = abs(n)
        #     ans = (x * self.myPow(x, n-1))
        #     bo = True
        # if n > 0:
        #     res = x * self.myPow(x, n-1)
        # if bo:
        #     return (1/ans)
        # return res
        #The above code is a very complex on time and space complexity
        bo = False
        if n < 0:
            n = abs(n)
            bo = True 
        if n == 0:
            return 1
        if n > 0:
            if n % 2:
                ans = x * self.myPow(x, n-1)
            else:
                ans = self.myPow(x, int(n/2))
                ans = ans * ans
        if bo:
            return (1/ans)
        return ans
