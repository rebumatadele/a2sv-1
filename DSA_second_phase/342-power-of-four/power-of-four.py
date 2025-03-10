class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        elif n < 1:
            return False
        if self.isPowerOfFour(n/4):
            return True
        else:
            return False

        
