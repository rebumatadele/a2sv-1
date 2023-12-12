class Solution:
    def isHappy(self, n: int) -> bool:
        test = 0
        c = 0
        size = len(str(n))
        while c < (2 * size +10):
            test = 0
            lst = list(str(n))
            lst = list(map(int, lst))
            for i in lst:
                test +=i**2
            n = test 
            c +=1

            if test == 1:
                return True
        return False